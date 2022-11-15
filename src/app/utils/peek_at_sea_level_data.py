import os
import xarray as xr
import dask as dst

cwd = os.getcwd()
dst=xr.open_mfdataset('/home/daria/PycharmProjects/bird_and_climate/cron_job/raw_data/sea_level/*.nc', concat_dim="time", combine="nested",
                  data_vars='minimal', coords='minimal', compat='override')

for i in dst.variables.keys():
    print(i)
    #print(dst[i].data)

print(dst.adt.data.blocks)
print("_________")
print(dst.adt.data.chunks)
print("_________")
print(dst.adt.data.ndim)
print(dst.adt.data.__dir__())
print("_________")
print(dst.adt.data.blocks[0, 0].compute())
print("________")
