import pytest
from logging import Logger
from pathlib import Path
from os import environ as env
from PyFHD.data_setup.uvfits import (
    extract_header,
    create_params,
    create_layout,
    extract_visibilities,
)
from PyFHD.data_setup.obs import create_obs
from PyFHD.io.pyfhd_io import convert_sav_to_dict
from PyFHD.io.pyfhd_io import recarray_to_dict
from PyFHD.io.pyfhd_io import save, load
import numpy.testing as npt
import numpy as np
from scipy.io import readsav
import importlib_resources


@pytest.fixture(
    scope="function",
    params=[
        "1088285600",
    ],
)
def obs_id(request):
    return request.param


def test_obs_creation(obs_id):
    # The obs creation test is more of an integration test, since we will be
    # using the extract_header, create_params, and create_layout to create the obs dictionary.
    # If this test pass then it essentially means that the dictionaries are almost identical
    # to that of the IDL structures in the ways that matter for a PyFHD run.
    # In this case we're only going to test the obs structure from run1 of each test.
    logger = Logger(1)
    pyfhd_config = {
        "obs_id": obs_id,
        "input_path": importlib_resources.files("PyFHD").joinpath(
            "resources/1088285600_example/"
        ),
        "n_pol": 2,
        "instrument": "mwa",
        "FoV": None,
        "dimension": 2048,
        "elements": 2048,
        "kbinsize": 0.5,
        "min_baseline": 1,
        "time_cut": None,
        "beam_nfreq_avg": 16,
        "dft_threshold": False,
        "healpix_inds": 1,
        "output_dir": ".",
        "override_target_phasera": None,
        "override_target_phasedec": None,
    }
    data_dir = importlib_resources.files("PyFHD").joinpath(
        "resources/test_data/data_setup/obs"
    )
    obs_fhd = load(data_dir / f"{obs_id}_obs.h5")
    pyfhd_header, params_data, antenna_header, antenna_data = extract_header(
        pyfhd_config, logger
    )
    params = create_params(pyfhd_header, params_data, logger)
    layout = create_layout(antenna_header, antenna_data, pyfhd_config, logger)
    obs = create_obs(pyfhd_header, params, layout, pyfhd_config, logger)

    vis_arr, vis_weights = extract_visibilities(
        pyfhd_header, params_data, pyfhd_config, logger
    )

    Path(pyfhd_config["output_dir"], "layout.h5").unlink()

    # Check the basic obs info
    assert obs["n_pol"] == obs_fhd["n_pol"]
    assert obs["n_tile"] == obs_fhd["n_tile"]
    assert obs["n_freq"] == obs_fhd["n_freq"]
    assert obs["n_time"] == obs_fhd["n_time"]
    assert obs["kpix"] == obs_fhd["kpix"]
    assert obs["dimension"] == obs_fhd["dimension"]
    assert obs["elements"] == obs_fhd["elements"]
    assert obs["n_baselines"] == obs_fhd["nbaselines"]
    assert vis_arr.shape == (
        obs["n_pol"],
        obs["n_freq"],
        obs["n_baselines"] * obs["n_time"],
    )
    assert vis_weights.shape == (
        obs["n_pol"],
        obs["n_freq"],
        obs["n_baselines"] * obs["n_time"],
    )
    npt.assert_almost_equal(obs["degpix"], obs_fhd["degpix"])
    npt.assert_almost_equal(obs["max_baseline"], obs_fhd["max_baseline"])
    npt.assert_almost_equal(obs["min_baseline"], obs_fhd["min_baseline"])
    npt.assert_array_equal(obs["pol_names"], obs_fhd["pol_names"].astype("str"))

    # Check baseline_info
    npt.assert_array_equal(
        obs["baseline_info"]["time_use"], obs_fhd["baseline_info"]["time_use"]
    )
    assert obs["n_time_flag"] == obs_fhd["n_time_flag"]
    npt.assert_array_equal(
        obs["baseline_info"]["tile_use"], obs_fhd["baseline_info"]["tile_use"]
    )
    # tile_flag is a little weird given it wants pointers from tile_flag
    # The indexes provided to tile_flag also go beyond the index range of the metadata
    # when producing the tile flags for the 3rd and 4th polarization is this a bug in FHD?
    # npt.assert_array_equal(obs['baseline_info']['tile_flag'], obs_fhd['baseline_info']['tile_flag'])
    assert obs["n_tile_flag"] == obs_fhd["n_tile_flag"]
    npt.assert_array_equal(
        obs["baseline_info"]["freq_use"], obs_fhd["baseline_info"]["freq_use"]
    )
    assert obs["dft_threshold"] == obs_fhd["dft_threshold"]
    npt.assert_array_equal(
        obs["baseline_info"]["tile_a"], obs_fhd["baseline_info"]["tile_a"]
    )
    npt.assert_array_equal(
        obs["baseline_info"]["tile_b"], obs_fhd["baseline_info"]["tile_b"]
    )
    npt.assert_array_equal(
        obs["baseline_info"]["tile_names"],
        np.char.strip((obs_fhd["baseline_info"]["tile_names"].astype("str"))).astype(
            int
        ),
    )

    # Check healpix
    assert obs["healpix"]["nside"] == obs_fhd["healpix"]["nside"]
    assert obs["healpix"]["n_pix"] == obs_fhd["healpix"]["n_pix"]
    assert obs["healpix"]["ind_list"] == int(obs_fhd["healpix"]["ind_list"])
    assert obs["healpix"]["n_zero"] == obs_fhd["healpix"]["n_zero"]
