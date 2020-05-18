import os
import numpy as np

# This nhis is the input clm frequency and also the output save frequency for the 
# corresponding offline sim.
nhiss = [1, 2, 5, 10, 20, 50, 100, 200, 500,1000,2000,5000]
whichadvects = ['U3C4']#,'MPDATA']
akss = [1e-6]#, 1e-3]  # vary background Aks values when Aks isn't being forced directly
aksflags = ['Akson', 'Aksoff']
clminputs = ['his']#, 'avg']

dts = [1,2,5,10,20]

# get absolute path for back one directory level for base of project
base = '/'.join(os.getcwd().split('/')[:-1])

dtbase = 20.0  # base case time step, seconds
ndays = 14  # number of simulation days

# whether to force offline from online his or online avg
for clminput in clminputs:
    # loop over input/output frequency
    for i, nhis in enumerate(nhiss):
        # loop over sim time step
        for dt in dts:
            if dt > nhis:  # can't have time step larger than output
                continue
            # nhis value in loop is incoming from the online case: how often output was saved.
            # nhis for the offline case should be chosen so the number of outputs matches the 
            # online case.
            # No, change it so that it outputs at the lowest option, 500
            if clminput == 'his':
                nhisoff = 500/dt
                navg = 0
            elif clminput == 'avg':
                nhisoff = 0
                navg = 500/dt
            # convert from number time steps to seconds for this time step
            # convert to form for inputting into .in file
            dtinput = str(dtbase*dt) + 'd0'
            # calculate number of time steps for offline sim. Take lower integer value
            # so we can't run out of input forcing.
            # still running out so subtract one time step to see if it fixes
            ntimes = np.floor(ndays*86400/(dtbase*dt)) - 2*nhis/dt - 1
            # loop over tracer advection scheme options
            for whichadvect in whichadvects:
                # Aks forcing can be turned on or off
                for aksflag in aksflags:
                    ## Update .in file ##
                    # input template and output version of .in file
                    infile_in = 'oil_off_ss.in'

                    ininame = '../oil_03/output_ss/%s/nhis%i/oil_03_his.nc' % (whichadvect,nhis) # start with his file
                    clminname = '../oil_03/output_ss/%s/nhis%i/oil_03_%s.nc' % (whichadvect,nhis,clminput)
                    
                    if clminput == 'avg':
                        # avg file does not include initial time step so access it from another file
                        clmname = '%s |\\\n%s' % (ininame, clminname)
                    elif clminput == 'his':
                        # his file includes its own first step
                        clmname = '%s' % (clminname)
                    
                    ## Update slurm file ##
                    jobfile_in = 'run_off_ss.slurm'

                    # if aks is not being forced, try different constant background values
                    if aksflag == 'Aksoff':

                        for aks in akss: 
                          
                            # exponent for Aks background
                            exp = int(abs(np.log10(aks)))

#                            ## Update .in file ##
#                            # input template and output version of .in file
                            infile_out = 'oil_off_ss_%s_%s_%s_nhis%i_dt%i_Aksbak%i.in' % (whichadvect, aksflag, clminput, nhis, dt, exp)

                            # form aks for input to .in file
                            aksinput = '1.0d-%i' % exp

                            # Substitute appropriate values in for placeholders in infile_in, then save changes to infile_out.
                            outdir = 'output_ss/%s/%s/Aksbak%i/%s/nhis%i' % (whichadvect,aksflag,exp,clminput,nhis)
                            hisname = '%s/oil_off_his_dt%i.nc' % (outdir,dt)
                            avgname = '%s/oil_off_avg_dt%i.nc' % (outdir,dt)
                            # make output directory
                            os.system('mkdir -p %s' % ('../'+outdir))
                            
                            strings = (nhisoff, navg, ntimes, dtinput, aksinput, hisname, avgname, ininame, clmname, base+'/External/'+infile_in, base+'/External/'+infile_out)
                            command = "sed -e 's/#NHIS#/%s/' -e 's/#NAVG#/%s/' -e 's/#NTIMES#/%s/' -e 's/#DT#/%s/' -e 's/#AKT_BAK#/%s/' -e 's|#HISNAME#|%s|' -e 's|#AVGNAME#|%s|' -e 's|#ININAME#|%s|' -e 's+#CLMNAME#+%s+' %s > %s"      
                            os.system(command % strings)


                            jobfile_out  = 'run_off_ss_%s_%s_Aksbak%i_%s_nhis%i_dt%i.slurm' % (whichadvect, aksflag, exp, clminput, nhis,dt)

                            logfile = 'ss_%s_%s_Aksbak%i_%s_nhis%i_dt%i' % (whichadvect,aksflag,exp,clminput,nhis,dt)

                            # set up slurm files
                            strings = (logfile, whichadvect, aksflag, infile_out, jobfile_in, jobfile_out)
                            os.system("sed -e 's/#LOGNAME#/%s/' -e 's/#WHICHADVECT#/%s/' -e 's/#AKSFLAG#/%s/' -e 's/#INFILE#/%s/' %s > %s" % strings)

                            os.chdir('../')
                            os.system('sbatch sub/%s' % jobfile_out)
                            os.chdir('./sub')

                    else:  # Aks is being forced

                        infile_out = 'oil_off_ss_%s_%s_%s_nhis%i_dt%i.in' % (whichadvect, aksflag, clminput, nhis, dt)

                        # Aks background isn't being varied here but input to placeholder. form aks for input to .in file
                        aksinput = '1.0d-%i' % 6

                        # Substitute appropriate values in for placeholders in infile_in, then save changes to infile_out.
                        outdir = 'output_ss/%s/%s/%s/nhis%i' % (whichadvect,aksflag,clminput,nhis)
                        hisname = '%s/oil_off_his_dt%i.nc' % (outdir,dt)
                        avgname = '%s/oil_off_avg_dt%i.nc' % (outdir,dt)
                        # make output directory
                        os.system('mkdir -p %s' % ('../'+outdir))

                        strings = (nhisoff, navg, ntimes, dtinput, aksinput, hisname, avgname, ininame, clmname, base+'/External/'+infile_in, base+'/External/'+infile_out)
                        command = "sed -e 's/#NHIS#/%s/' -e 's/#NAVG#/%s/' -e 's/#NTIMES#/%s/' -e 's/#DT#/%s/' -e 's/#AKT_BAK#/%s/' -e 's|#HISNAME#|%s|' -e 's|#AVGNAME#|%s|' -e 's|#ININAME#|%s|' -e 's+#CLMNAME#+%s+' %s > %s"
                        os.system(command % strings)

                        jobfile_out  = 'run_off_ss_%s_%s_%s_nhis%i_dt%i.slurm' % (whichadvect, aksflag, clminput, nhis,dt)
                       
                        logfile = 'ss_%s_%s_%s_nhis%i_dt%i' % (whichadvect,aksflag,clminput,nhis,dt)

                        # set up slurm files
                        strings = (logfile, whichadvect, aksflag, infile_out, jobfile_in, jobfile_out)
                        os.system("sed -e 's/#LOGNAME#/%s/' -e 's/#WHICHADVECT#/%s/' -e 's/#AKSFLAG#/%s/' -e 's/#INFILE#/%s/' %s > %s" % strings)


                        os.chdir('../')
                        os.system('sbatch sub/%s' % jobfile_out)
                        os.chdir('./sub')

