# This script prints the individual wget urls for each variable and each day. 

# Load python modules
import pandas as pd
import datetime
import os
import sys
import xarray as xr
import numpy as np

# Retrieve user editable variables
year_start = sys.argv[1]
year_end = sys.argv[2]

month_start = sys.argv[3]
month_end = sys.argv[4]

day_start = sys.argv[5]
day_end = sys.argv[6]

lat_min = float(sys.argv[7])
lat_max = float(sys.argv[8])
lon_min = float(sys.argv[9])
lon_max = float(sys.argv[10])

### Calculate the indices for the bounding box. M2LL.nc is (all) the MERRA-2 grid coordinates. (MS)
m2ll = xr.open_dataset('M2LL.nc')
ilon_min,ilon_max = np.where((m2ll.lon.values>=lon_min) & (m2ll.lon.values<=lon_max))[0][[0,-1]]
ilat_min,ilat_max = np.where((m2ll.lat.values>=lat_min) & (m2ll.lat.values<=lat_max))[0][[0,-1]]
m2ll.close()
vext = f'[0:23][{ilat_min}:{ilat_max}][{ilon_min}:{ilon_max}]' # this is the string extension for each variable to set the bounding box
###

# Create date object
date = pd.date_range(start = str(month_start) + "/" + str(day_start) + "/" + str(year_start), \
    end =str(month_end) + "/" + str(day_end) + "/" + str(year_end))

# Define file names and delete old versions
surface_wget_url_file = "./surface/wget_surface.sh"
if os.path.exists(surface_wget_url_file):
    os.remove(surface_wget_url_file)
precip_wget_url_file = "./precip/wget_precip.sh"
if os.path.exists(precip_wget_url_file):
    os.remove(precip_wget_url_file)
radiation_wget_url_file = "./radiation/wget_radiation.sh"
if os.path.exists(radiation_wget_url_file):
    os.remove(radiation_wget_url_file)
evap_wget_url_file = "./evap/wget_evap.sh"
if os.path.exists(evap_wget_url_file):
    os.remove(evap_wget_url_file)

# Write URLs
for day in range(0, len(date)):

    day_str = date[day].strftime('%Y%m%d')
    day_year = date[day].year
    day_month = date[day].month
    if day_month < 10:
        day_month = "0" + str(day_month)

    stream = "-999"
    if day_year >= 1980 and  day_year <= 1990:
        stream = "100"
    elif day_year > 1990 and  day_year <= 2000:
        stream = "200"
    elif day_year > 2000 and  day_year <= 2010:
        stream = "300"
    elif day_year == 2020 and day_month == "09":
        stream = "401"
    else:
        stream = "400"
        
    ##### Surface #####
    surface_file = open(surface_wget_url_file, "a")
    m2_vars = ['H500','PS','QV2M','T2M','TS','U10M','V10M']
    m2v_ext = [s+vext for s in m2_vars]
    m2v_cat = ','.join(m2v_ext) + f',time,lat[{ilat_min}:{ilat_max}],lon[{ilon_min}:{ilon_max}]'
    surface_str = f"https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXSLV.5.12.4/{day_year}/{day_month}/MERRA2_{stream}.tavg1_2d_slv_Nx.{day_str}.nc4.nc4?" + m2v_cat + "\n"
    surface_file.write(surface_str)
    surface_file.close()

    ##### Precipitation #####
    precip_file = open(precip_wget_url_file, "a")
    m2_vars = ['PRECCU','PRECLS','PRECSN']
    m2v_ext = [s+vext for s in m2_vars]
    m2v_cat = ','.join(m2v_ext) + f',time,lat[{ilat_min}:{ilat_max}],lon[{ilon_min}:{ilon_max}]'
    precip_str = f"https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXINT.5.12.4/{day_year}/{day_month}/MERRA2_{stream}.tavg1_2d_int_Nx.{day_str}.nc4.nc4?" + m2v_cat + "\n"
    precip_file.write(precip_str)
    precip_file.close()

    ##### Radiation #####
    radiation_file = open(radiation_wget_url_file, "a")
    m2_vars = ['LWGAB','LWGEM','LWGNT','SWGDN','SWGNT','ALBEDO','TS']
    m2v_ext = [s+vext for s in m2_vars]
    m2v_cat = ','.join(m2v_ext) + f',time,lat[{ilat_min}:{ilat_max}],lon[{ilon_min}:{ilon_max}]'
    radiation_str = f"https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXRAD.5.12.4/{day_year}/{day_month}/MERRA2_{stream}.tavg1_2d_rad_Nx.{day_str}.nc4.nc4?" + m2v_cat + "\n"
    radiation_file.write(radiation_str)
    radiation_file.close()

    ##### Evaporation #####
    evap_file = open(evap_wget_url_file, "a")
    m2_vars = ['EVAP']
    m2v_ext = [s+vext for s in m2_vars]
    m2v_cat = ','.join(m2v_ext) + f',time,lat[{ilat_min}:{ilat_max}],lon[{ilon_min}:{ilon_max}]'
    evap_str = f"https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXFLX.5.12.4/{day_year}/{day_month}/MERRA2_{stream}.tavg1_2d_flx_Nx.{day_str}.nc4.nc4?" + m2v_cat + "\n"
    evap_file.write(evap_str)
    evap_file.close()

