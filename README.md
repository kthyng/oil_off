# oil_off
Bio offline test with oil application
This test runs the fennel biology offline using climatology files and my 'offline' branch of COAWST-ROMS-OIL version of ROMS.
The climatology is generated from the history files from Dmitry's oil run (make script are on the nc_make_files folder)

## How to run an offline simulation

1. Run an online simulation
2. As a starting place, use files like:
  - `python build-coawst.py --clean --mpi  oil_offline_kmt`: convenient way to compile your simulation, but not necessary
  - `Include/oil_offline_kmt.h`: already has flags set up for offline simulation. However, it is currently set up to read in a lot of variables that you might not have saved in your online simulation. Look in file for guidance on this.
  - `External/ocean_oil_offline_dt00020_clm20secs_LeftGaussian.in`: many inputs in here are specific to offline simulation, but should change especially input and output file locations to match your simulation. Note that VARNAME *HAS* to match the location of the file for the offline COAWST oil code or you will get a segfault.
  - `sbatch sub/run_oil_dt00020_clm1hr_FloatTracer.slurm`: for TAMU clusters to run simulation
