import xarray as xr
from datetime import datetime
import os

def make_clm(input_file, output_name):
    
    #assert os.path.exists(input_file), ('%s does not exist.' % input_file)
    
    keep = ['ocean_time', 'zeta', 'ubar', 'vbar', 'u', 'v', 'w', 'omega', 'temp', 'salt']
    tnames = ['zeta_time', 'u2d_time', 'v2d_time', 'u3d_time', 'v3d_time', 'ocean_time',
                'ocean_time', 'temp_time', 'salt_time']
                
    nfiles = len(input_file)
    if nfiles==1:
        ds = xr.open_dataset(input_file, decode_times=False)
    elif nfiles>1:
        ds = xr.open_mfdataset(input_file, decode_times=False)
    else:
        print('no input files found')
    clm = ds.copy()
        
    for var in clm.data_vars:
        if var not in keep:
            clm = clm.drop(var)
            
    for attr in ds.attrs:
        del(clm.attrs[attr])
        
    clm.attrs['Author'] = 'VRX'
    clm.attrs['Description'] = 'Climatology for offline simulation'
    clm.attrs['Created'] = datetime.now().isoformat()
    clm.attrs['type'] = 'ROMS CLM file'

    
    #########################################
    for var, tname in zip(keep[1:], tnames):
        
        clm[var].coords[tname] = clm.ocean_time
        clm[var].attrs['long_name'] = clm[var].long_name + ' climatology'
        if tname != 'ocean_time':
            clm[var] = clm[var].rename({'ocean_time':tname})
            clm[var].attrs['time'] = tname
            clm[tname].attrs['long_name'] = 'time for '+clm[var].long_name
            clm[tname].attrs['field'] = tname +", scalar, series"
    print('creating %s' % output_name)        
    print(clm.data_vars) 
    clm.to_netcdf(output_name)
    
if __name__ == '__main__':
    import glob

    files = sorted(glob.glob('../../oil_03/output_LeftGaussian/30mins/oil_03_ocean_avg_*'))
    make_clm(input_file=files, output_name='../clm/oil_clm_avg_30mins.nc')
    

