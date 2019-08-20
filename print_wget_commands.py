# This script prints the individual wget urls for each variable and each day. 

# Load python modules
import pandas as pd
import datetime
import os

# Define user editable variables
year_start = 1980
year_end = 1980

lat_min = "-90"
lat_max = "-40"
lon_min = "-180"
lon_max = "180"

# Create date object
date = pd.date_range(start='1/1/' + str(year_start), end='12/31/' + str(year_end))

# Define file names and delete old versions
surface_wget_url_file = "./surface/wget_surface.sh"
os.remove(surface_wget_url_file)
precip_wget_url_file = "./precip/wget_precip.sh"
os.remove(precip_wget_url_file)
radiation_wget_url_file = "./radiation/wget_radiation.sh"
os.remove(radiation_wget_url_file)

# Write URLs
# for day in range(0, len(date)):
for day in range(0, 3):

	day_str = date[day].strftime('%Y%m%d')
	day_year = date[day].year

	##### Surface #####
	surface_file = open(surface_wget_url_file, "a")

	surface_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXSLV.5.12.4%2F" + str(day_year) + "%2F01%2FMERRA2_100.tavg1_2d_slv_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + lat_min + "%2C" + lon_min + "%2C" + lat_max + "%2C" + lon_max \
		+ "&LABEL=MERRA2_100.tavg1_2d_slv_Nx.19800101.SUB.nc4&SHORTNAME=M2T1NXSLV&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=ps%2Cqv2m%2Ct2m%2Cts%2Cu10m%2Cv10m\n"

	surface_file.write(surface_str)
	surface_file.close()

	##### Precipitation #####
	precip_file = open(precip_wget_url_file, "a")

	precip_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXINT.5.12.4%2F" + str(day_year) + "%2F01%2FMERRA2_100.tavg1_2d_int_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + lat_min + "%2C" + lon_min + "%2C" + lat_max + "%2C" + lon_max \
		+ "&LABEL=MERRA2_100.tavg1_2d_int_Nx.19800101.SUB.nc4&SHORTNAME=M2T1NXINT&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=preccu%2Cprecls%2Cprecsn\n"

	precip_file.write(precip_str)
	precip_file.close()

	##### Radiation #####
	radiation_file = open(radiation_wget_url_file, "a")

	radiation_str = "http://goldsmr4.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=" \
		+ "%2Fdata%2FMERRA2%2FM2T1NXRAD.5.12.4%2F" + str(day_year) + "%2F01%2FMERRA2_100.tavg1_2d_rad_Nx." \
		+ day_str \
		+ ".nc4&FORMAT=bmM0Lw&BBOX=" + lat_min + "%2C" + lon_min + "%2C" + lat_max + "%2C" + lon_max \
		+ "&LABEL=MERRA2_100.tavg1_2d_rad_Nx.19800101.SUB.nc4&SHORTNAME=M2T1NXRAD&SERVICE=SUBSET_ME" \
		+ "RRA2&VERSION=1.02&LAYERS=&VARIABLES=lwgab%2Clwgem%2Clwgnt%2Cswgdn%2Cswgnt\n"

	radiation_file.write(radiation_str)
	radiation_file.close()


