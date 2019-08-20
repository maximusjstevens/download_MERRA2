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

# Write URLs
for day in range(0, len(date)):

	day_str = date[day].strftime('%Y%m%d')
	day_year = date[day].year
	day_month = date[day].month
	if day_month < 10:
		day_month = "0" + str(day_month)

	##### Surface #####
	surface_file = open(surface_wget_url_file, "a")

	surface_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXSLV.5.12.4%2F" + str(day_year) + "%2F" + str(day_month) + "%2FMERRA2_100.tavg1_2d_slv_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + str(lat_min) + "%2C" + str(lon_min) + "%2C" + str(lat_max) + "%2C" + str(lon_max) \
		+ "&LABEL=MERRA2_100.tavg1_2d_slv_Nx." + str(day_str) + ".SUB.nc4&SHORTNAME=M2T1NXSLV&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=ps%2Cqv2m%2Ct2m%2Cts%2Cu10m%2Cv10m\n"

	surface_file.write(surface_str)
	surface_file.close()

	##### Precipitation #####
	precip_file = open(precip_wget_url_file, "a")

	precip_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXINT.5.12.4%2F" + str(day_year) + "%2F" + str(day_month) + "%2FMERRA2_100.tavg1_2d_int_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + str(lat_min) + "%2C" + str(lon_min) + "%2C" + str(lat_max) + "%2C" + str(lon_max) \
		+ "&LABEL=MERRA2_100.tavg1_2d_int_Nx." + str(day_str) + ".SUB.nc4&SHORTNAME=M2T1NXINT&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=preccu%2Cprecls%2Cprecsn\n"

	precip_file.write(precip_str)
	precip_file.close()

	##### Radiation #####
	radiation_file = open(radiation_wget_url_file, "a")

	radiation_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXRAD.5.12.4%2F" + str(day_year) + "%2F" + str(day_month) + "%2FMERRA2_100.tavg1_2d_rad_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + str(lat_min) + "%2C" + str(lon_min) + "%2C" + str(lat_max) + "%2C" + str(lon_max) \
		+ "&LABEL=MERRA2_100.tavg1_2d_rad_Nx." + str(day_str) + ".SUB.nc4&SHORTNAME=M2T1NXRAD&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=lwgab%2Clwgem%2Clwgnt%2Cswgdn%2Cswgnt\n"

	radiation_file.write(radiation_str)
	radiation_file.close()


