import os

clim_list = ['10mins', '30mins', '1hr', '2hrs', '3hrs']
dt_list = [20, 120, 450, 900, 1800]

JobL = 'FloatTracer_hisclm'
floatin = 'gaussian_floats.in'
path = '/home/lixinqu/scratch/projects/CSOMIO/oil_off/OUTPUT/%s' % JobL

for clm in clim_list:
    for dt in dt_list:
        clmfile = 'oil_clm_his_%s.nc' % clm

        infileT = '../External/ocean_oil_offline_dt%05d.in' % dt
        infile = '../External/ocean_oil_offline_dt%05d_clm%s_%s.in' % (dt,clm,JobL)
        infileSED = 'ocean_oil_offline_dt%05d_clm%s_%s.in' % (dt,clm,JobL)

        jobfileT = 'run_oil.slurm'
        jobfile  = 'run_oil_dt%05d_clm%s_%s.slurm' % (dt,clm,JobL)

        outdir = path + '/clm_%s/dt_%05d' % (clm,dt)
        outSED = path + '/clm_%s' % (clm)

        logfile = 'OFFLINE_dt%05d_clm%s_%s' % (dt,clm,JobL)

        os.system('mkdir -p %s' % outdir)
        os.system("sed -e 's/#CLMNAME#/%s/g' -e 's|#OUTPUTPATH#|%s|g' -e 's/#FLOATFILE#/%s/g' %s > %s" % (clmfile, outSED, floatin, infileT, infile))
        os.system("sed -e 's/#LOGNAME#/%s/g' -e 's|#ROMSINNAME#|%s|g' %s > %s" % (logfile, infileSED, jobfileT, jobfile))

        os.chdir('../')
        os.system('sbatch sub/%s' % jobfile)
        os.chdir('./sub')

