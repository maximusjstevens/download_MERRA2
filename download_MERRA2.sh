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

year_start="2019"
year_end="2019"

month_start="1"
month_end="12"

day_start="1"
day_end="31"

# Currently this script only supports the following lat/lon box. Need to change the indices in print_wget_commands to bring back this functionality
lat_min="-90"
lat_max="-40"
lon_min="-180"
lon_max="180"

##### End User Editable Variables #####

# First print wget commands to files
python3 print_wget_commands.py ${year_start} ${year_end} ${month_start} ${month_end} \
	${day_start} ${day_end} ${lat_min} ${lat_max} ${lon_min} ${lon_max}

# Now run wget to retrieve data
bash retrieve_data.sh

# Process files into .nc
rm nc_files/*.nc
csh create_forcing_nc.sh $year_start $year_end
