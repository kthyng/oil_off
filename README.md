[![DOI](https://zenodo.org/badge/250293006.svg)](https://zenodo.org/badge/latestdoi/250293006)

# oil_off

Force a passive tracer field using output from an [online simulation](https://github.com/kthyng/oil_03) input as climatology files.

## How to run an offline simulation

1. Run an online simulation with a special version of COAWST/ROMS: https://github.com/kthyng/COAWST-ROMS-OIL
2. Run your offline sim:
  - You can compile your code with `python build-coawst.py --clean --mpi  oil_offline`
  - Start from `Include/oil_offline.h` to choose your preprocessor flags. Good choices are already selected there.
    - Use OUT_DOUBLE for best results
    - AKSCLIMATOLOGY to force Aks from the online simulation
    - OFFLINE and OFFLINE_TPASSIVE
    - MPDATA for tracer advection gives best results (as compared with TS_U3HADVECTION and TS_C4VADVECTION together)
  - Use `External/ocean_oil_offline.in` as a template.
    - Set output from online simulation as clm input
    - if forcing with an avg file from online simulation, need to place a file containing the initial conditions first
    - choose offline simulation time step: time step needs to factor into online output evenly
    - can't have time step larger than online output
    - There should be no forcing in the offline simulation since it all comes in through the online output as climatology
      - Boundaries should all be closed except for dye_01 since all boundary information is encoded in the online output
      - Turn off river forcing
      - Do not force winds, bulk fluxes, etc
      - No nudging to climatology
      - do include clm for zeta, m2, m3
      - only output dye_01 and zeta since otherwise best to use online output (w for example is not calculated correctly in offline sim)
      - VARNAME points to a special offline simulation version of varinfo.dat, which should be redirected to wherever your version of this [ROMS/COAWST](https://github.com/kthyng/COAWST-ROMS-OIL) is.
  - `sbatch sub/run_oil.slurm`: example file for slurm clusters to run simulation
