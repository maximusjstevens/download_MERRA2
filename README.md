# download_MERRA2

## This repository contains scripts to automatically download and process MERRA-2 atmospheric reanalysis. 
#### To begin, first clone this directory. Then, modify user editable variables in download_MERRA2.sh in order to match your variable, temporal, and spatial preferences. Next, execute the following command in your terminal window to initialize the workflow. 
#### $ bash download_MERRA2.sh

## Dependencies:
* Python3 (https://www.python.org/download/releases/3.0/)
* Pandas (https://pandas.pydata.org)
* CDO (https://code.mpimet.mpg.de/projects/cdo/)
* Wget (https://www.gnu.org/software/wget/)

## NASA EarthData Login
#### In order to retrieve MERRA-2 you will need to create a NASA EarthData login (https://urs.earthdata.nasa.gov/). You will then need to allow access to the NASA GESDISC Data archive. Additionally, to store password credentials for automatic data retrievals, initialize a .netrc file directed to urs.earthdata.nasa.gov and an empy .urs_cookies file (https://wiki.earthdata.nasa.gov/display/HDD/Wget+with+URS+Authentication#WgetwithURSAuthentication-Step-by-stepguide). 

## Acknowledgments
#### I would like to acknowledge Richard Cullather for providing instructions on using Wget and Jan Lenaerts for providing starter scripts on processing Wget output into netCDF files. 
