# This script prints the individual wget urls for each variable and each day. 

# Load python modules
import pandas as pd
import datetime
import os
import sys

# Retrieve user editable variables
year_start = sys.argv[1]
year_end = sys.argv[2]

month_start = sys.argv[3]
month_end = sys.argv[4]

day_start = sys.argv[5]
day_end = sys.argv[6]

lat_min = sys.argv[7]
lat_max = sys.argv[8]
lon_min = sys.argv[9]
lon_max = sys.argv[10]

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
		stream = "1"
	elif day_year > 1990 and  day_year <= 2000:
		stream = "2"
	elif day_year > 2000 and  day_year <= 2010:
		stream = "3"
	else:
		stream = "4"

	##### Surface #####
	surface_file = open(surface_wget_url_file, "a")
	surface_str = "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXSLV.5.12.4/" + str(day_year) + "/" + str(day_month) + "/MERRA2_" + str(stream) + "00.tavg1_2d_slv_Nx." + str(day_str) + ".nc4.nc4?H500[0:23][0:100][0:575],time,lat[0:100],lon[0:575]\n"
	surface_file.write(surface_str)
	surface_file.close()

	##### Precipitation #####
	precip_file = open(precip_wget_url_file, "a")
	precip_str = "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXINT.5.12.4/" + str(day_year) + "/" + str(day_month) + "/MERRA2_" + str(stream) + "00.tavg1_2d_int_Nx." + str(day_str) + ".nc4.nc4?PRECCU[0:23][0:100][0:575],PRECLS[0:23][0:100][0:575],PRECSN[0:23][0:100][0:575],time,lat[0:100],lon[0:575]\n"
	precip_file.write(precip_str)
	precip_file.close()

	##### Radiation #####
	radiation_file = open(radiation_wget_url_file, "a")
	radiation_str = "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXRAD.5.12.4/" + str(day_year) + "/" + str(day_month) + "/MERRA2_" + str(stream) + "00.tavg1_2d_rad_Nx." + str(day_str) + ".nc4.nc4?LWGAB[0:23][0:100][0:575],LWGEM[0:23][0:100][0:575],LWGNT[0:23][0:100][0:575],SWGDN[0:23][0:100][0:575],SWGNT[0:23][0:100][0:575],time,lat[0:100],lon[0:575]\n"
	radiation_file.write(radiation_str)
	radiation_file.close()

	##### Evaporation #####
	evap_file = open(evap_wget_url_file, "a")
	evap_str = "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXFLX.5.12.4/" + str(day_year) + "/" + str(day_month) + "/MERRA2_" + str(stream) + "00.tavg1_2d_flx_Nx." + str(day_str) + ".nc4.nc4?EVAP[0:23][0:100][0:575],time,lat[0:100],lon[0:575]\n"
	evap_file.write(evap_str)
	evap_file.close()

