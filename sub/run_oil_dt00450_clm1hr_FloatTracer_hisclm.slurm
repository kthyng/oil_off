#!/bin/bash
##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION
#SBATCH --export=NONE                #Do not propagate environment
#SBATCH --get-user-env=L             #Replicate login environment

##NECESSARY JOB SPECIFICATIONS
#SBATCH --job-name=ngom_online       #Set the job name to "JobExample2"
#SBATCH --time=3:00:00               #Set the wall clock limit to 6hr and 30min
#SBATCH --nodes=1                    #Request 1 node
#SBATCH --ntasks-per-node=28         #Request 8 tasks/cores per node
#SBATCH --mem=8G                    #Request 8GB per node 
#SBATCH --output=./log/OFFLINE_dt00450_clm1hr_FloatTracer_hisclm.%j      #Send stdout/err to "Example2Out.[jobID]" 

##OPTIONAL JOB SPECIFICATIONS
##SBATCH --account=123456             #Set billing account to 123456
##SBATCH --mail-type=ALL              #Send email on all job events
##SBATCH --mail-user=lixinqu@tamu.edu    #Send all emails to email_address 

#First Executable Line

# load intel toolchain
module load netCDF-Fortran/4.4.4-intel-2016a
module load netCDF/4.4.0-intel-2016a

export NETCDF=$EBROOTNETCDFMINFORTRAN
export NETCDF_INCDIR=$EBROOTNETCDFMINFORTRAN/include
export NETCDF_LIBDIR=$EBROOTNETCDFMINFORTRAN/lib

export MCT_INCDIR=/home/lixinqu/local/include
export MCT_LIBDIR=/home/lixinqu/local/lib

mpirun -np 28 ./coawstM ./External/ocean_oil_offline_dt00450_clm1hr_FloatTracer_hisclm.in
