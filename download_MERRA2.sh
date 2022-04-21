#!/bin/bash

# This scipt will download and process MERRA-2 data. 
# To run this script, execute the following command in the terminal:
# $ bash download_MERRA2.sh

# Current functionality: Currently this script downloads MERRA-2 surface meteorology (pressure, specific humidity,
# 2 m temperature, surface temperature, 10 m u and v winds), precipitation (convective rain, large scale rain, 
# snowfall), and radiation (absorbed, emitted, and net longwave and donwelling and net shortwave). In order to 
# change these variables, change print_wget_commands.py. To get example Wget urls visit this link
#  (https://disc.gsfc.nasa.gov/daac-bin/FTPSubset2.pl). 

# To Do:
# 1. Add functionality to automatically change the retrieved variables.
# 2. Add functionality to allow for retriveing of daily, hourly, monthly data. 

##### Begin User Editable Variables #####

year_start="2020"
year_end="2020"

month_start="1"
month_end="1"

day_start="1"
day_end="3"

# Set the bounding box for spatial extent
lat_min="55"
lat_max="90"
lon_min="-80"
lon_max="-10"

datapath=$PWD #If you want to download and save the files to the current directory (and subdirectories)
# datapath="/PATH/TO/DIRECTORY" # Put the downloaded files somewhere else.

##### End User Editable Variables #####

# First print wget commands to files
python3 print_wget_commands.py ${year_start} ${year_end} ${month_start} ${month_end} \
	${day_start} ${day_end} ${lat_min} ${lat_max} ${lon_min} ${lon_max}

# Now run wget to retrieve data
bash retrieve_data.sh $datapath

# Process files into individual .nc files for each variable, for each year
mkdir -p "$datapath/nc_files"
rm "$datapath/nc_files/*.nc"
csh create_forcing_nc.sh $year_start $year_end $datapath
