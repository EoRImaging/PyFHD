# Installation

The dependencies on PyFHD to run with FHD have been removed, this makes installing and `PyFHD` much easier than FHD. `PyFHD` is currently supported for Python 3.10+.

## pip

PyFHD is on [PyPi](https://pypi.org/). The pip installation assumes you have already created a **virtual environment** using `uv`, `mamba` or `venv` as per best practice.

```bash
pip install pyfhd
```

You can Verify the installation using the version command
    
```bash
    pyfhd -v
```

It should give you output that looks like this:

```
    ________________________________________________________________________
    |    ooooooooo.               oooooooooooo ooooo   ooooo oooooooooo.    |
    |    8888   `Y88.             8888       8 8888    888   888     Y8b    |
    |    888   .d88' oooo    ooo  888          888     888   888      888   |
    |    888ooo88P'   `88.  .8'   888oooo8     888ooooo888   888      888   |
    |    888           `88..8'    888          888     888   888      888   |
    |    888            `888'     888          888     888   888     d88'   |
    |    o888o            .8'     o888o        o888o   o888o o888bood8P'    |
    |                 .o..P'                                                |
    |                `Y8P'                                                  |
    |_______________________________________________________________________|
    
    Python Fast Holographic Deconvolution 

    Translated from IDL to Python as a collaboration between Astronomy Data and Computing Services (ADACS) and the Epoch of Reionisation (EoR) Team.

    Repository: https://github.com/ADACS-Australia/PyFHD

    Documentation: https://pyfhd.readthedocs.io/en/latest/

    Version: 1.0

    Git Commit Hash: 176fa3aaf9aeca44b38f00ac4745d9b3a9eefe9c (tutorial_adjustments)
```

## Installing for additional development?

Please follow the contribution guide.