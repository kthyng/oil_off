#!/bin/bash
##ENVIRONMENT SETTINGS; CHANGE WITH CAUTION
#SBATCH --export=NONE                #Do not propagate environment
#SBATCH --get-user-env=L             #Replicate login environment

##NECESSARY JOB SPECIFICATIONS
#SBATCH --job-name=oil_offline       #Set the job name to "JobExample2"
#SBATCH --time=6:00:00               #Set the wall clock limit to 6hr and 30min
#SBATCH --nodes=5                    #Request 1 node
#SBATCH --ntasks-per-node=28         #Request 8 tasks/cores per node
#SBATCH --mem=8G                    #Request 8GB per node 
#SBATCH --output=NGOM_Out.%j      #Send stdout/err to "Example2Out.[jobID]" 

##OPTIONAL JOB SPECIFICATIONS
##SBATCH --account=123456             #Set billing account to 123456
##SBATCH --mail-type=ALL              #Send email on all job events
##SBATCH --mail-user=vrx@tamu.edu    #Send all emails to email_address 

#First Executable Line

# load intel toolchain
module load netCDF/4.6.1-intel-2018b
module load netCDF-Fortran/4.4.4-intel-2018b
module load flex

mpirun -np 140 ./coawstG External/ocean_oil_offline.in
