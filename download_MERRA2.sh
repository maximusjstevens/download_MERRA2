#!/bin/bash

# This scipt will download and process MERRA-2 data. 
# To run this script, execute the following command in the terminal:
# $ bash download_MERRA2.sh

# To Do
# 1. Add blurb about creating a NASA login
# 2. Update script for user editable variables. 

# First print wget commands to files
python3 print_wget_commands.py

# Now run wget to retrieve data
bash retrieve_data.sh

# Process files into .nc
csh create_forcing_nc.sh