#!/bin/bash

# This scipt will download and process MERRA-2 data. 
# In order to specify variables and times. Edit print_wget_commands.py and create_forcing_nc.sh

# To run the script execute the following command in the terminal:
# $ bash download_MERRA2.sh

# To Do
# 3. Make this scipt contain user editable variables. 
# 4. Add documentation about creating a login. 
# 5. Add README information on github.

# Dependencies
# 1. CDO (url linked here)
# 2. python3


# First print wget commands to files
python3 print_wget_commands.py

# Now run wget to retrieve data
bash retrieve_data.sh

# Process files into .nc
csh create_forcing_nc.sh