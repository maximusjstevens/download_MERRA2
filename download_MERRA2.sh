#!/bin/bash

# This scipt will download and process MERRA-2 data. 
# To run this script, execute the following command in the terminal:
# $ bash download_MERRA2.sh

# To Do
# 1. Update script for user editable variables. 

##### Begin User Editable Variables #####

year_start="1980"
year_end="1980"

month_start="1"
month_end="12"

day_start="1"
day_end="31"

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
csh create_forcing_nc.sh
