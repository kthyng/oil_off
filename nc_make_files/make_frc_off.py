import xarray as xr
from datetime import datetime
import os
import glob

def make_ini(frc_name='../../oil_03/oil_03_frc.nc',
             his_name='../../oil_03/oil_03_ocean_his.nc',
             output_name='../INPUT/oil_frc_off.nc'):
    
    #assert os.path.exists(rootdir), ('%s does not exist.' % rootdir)
                
    his = xr.open_mfdataset(his_name, decode_times=False)
    frc = xr.open_dataset(frc_name, decode_times=False)
    
    add = ['shflux', 'sustr', 'svstr', 'bustr', 'bvstr']
    
    for var in add:
        frc[var] = his[var]

    frc.attrs['Author'] = 'VRX'
    frc.attrs['Description'] = 'Modified forcing for offline simulation, made from: '+ his.file+' and forcing'
    frc.attrs['Created'] = datetime.now().isoformat()
    frc.attrs['type'] = 'ROMS FRC file'
 
    print('creating %s' % output_name)
    print(frc.data_vars) 
    frc.to_netcdf(output_name)
    
if __name__ == '__main__':

    make_ini(his_name=glob.glob('../../oil_03/*ocean_his*.nc'))
