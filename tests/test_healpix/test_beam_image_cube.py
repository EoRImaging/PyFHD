from os import environ as env
from pathlib import Path
import numpy as np
import numpy.testing as npt
import pytest
from logging import Logger
from PyFHD.io.pyfhd_io import convert_sav_to_dict, load, recarray_to_dict, save
from PyFHD.healpix.healpix_utils import beam_image_cube


@pytest.fixture
def data_dir():
    return Path(env.get("PYFHD_TEST_PATH"), "healpix", "beam_image_cube")


@pytest.fixture(
    scope="function",
    params=["1088285600", "1088716296", "point_zenith", "point_offzenith"],
)
def tag(request):
    return request.param


@pytest.fixture(scope="function", params=["run3", "run4"])
def run(request):
    return request.param


@pytest.fixture
def beam_dir():
    return Path(env.get("PYFHD_TEST_PATH"), "beams")


skip_tests = [
    ["1088285600", "run4"],
    ["point_zenith", "run3"],
    ["point_offzenith", "run3"],
    ["1088716296", "run3"],
]


@pytest.fixture
def before_file(tag, run, data_dir):
    if [tag, run] in skip_tests:
        return None
    before_file = Path(data_dir, f"{tag}_{run}_before_{data_dir.name}.h5")
    # If the h5 file already exists and has been created, return the path to it
    if before_file.exists():
        return before_file

    sav_file = before_file.with_suffix(".sav")
    sav_dict = convert_sav_to_dict(str(sav_file), "faked")
    sav_dict = recarray_to_dict(sav_dict)

    save(before_file, sav_dict, "sav_dict")

    return before_file


@pytest.fixture()
def after_file(tag, run, data_dir):
    if [tag, run] in skip_tests:
        return None
    after_file = Path(data_dir, f"{tag}_{run}_after_{data_dir.name}.h5")
    # If the h5 file already exists and has been created, return the path to it
    if after_file.exists():
        return after_file

    sav_file = after_file.with_suffix(".sav")
    sav_dict = convert_sav_to_dict(str(sav_file), "faked")
    sav_dict = recarray_to_dict(sav_dict)

    save(after_file, sav_dict["beam_arr"], "beam_arr")

    return after_file


def test_beam_image_cube(before_file, after_file, beam_dir):
    if before_file == None or after_file == None:
        pytest.skip(
            f"This test has been skipped because the test was listed in the skipped tests due to FHD not outputting them: {skip_tests}"
        )

    h5_before = load(before_file)
    expected_beam_arr = np.swapaxes(load(after_file), 0, 1)

    psf = load(Path(beam_dir, "decomp_beam_pointing0.h5"), lazy_load=True)

    h5_before["obs"]["dimension"] = int(h5_before["obs"]["dimension"])
    h5_before["obs"]["elements"] = int(h5_before["obs"]["elements"])

    beam_arr, beam_mask = beam_image_cube(
        h5_before["obs"],
        psf,
        Logger(1),
        n_freq_bin=h5_before["n_freq_bin"],
        beam_threshold=h5_before["beam_threshold"],
        square=h5_before["square"],
    )

    npt.assert_allclose(beam_arr, expected_beam_arr, atol=1e-8)
