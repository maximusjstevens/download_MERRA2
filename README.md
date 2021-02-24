[![DOI](https://zenodo.org/badge/203448170.svg)](https://zenodo.org/badge/latestdoi/203448170)

# download_MERRA2

## This repository contains scripts to automatically download and process MERRA-2 atmospheric reanalysis. 
#### To begin, first clone this directory. Then modify user editable variables in `download_MERRA-2.sh`. 

#### Next, execute the following command in your terminal window to initialize the workflow. 
#### `$ bash download_MERRA2.sh`

## Dependencies:
* Python3 (https://www.python.org/download/releases/3.0/)
* Pandas (https://pandas.pydata.org)
* CDO (https://code.mpimet.mpg.de/projects/cdo/)
* Wget (https://www.gnu.org/software/wget/)

## NASA EarthData Login
#### In order to retrieve MERRA-2 you will need to create a NASA EarthData login (https://urs.earthdata.nasa.gov/). You will then need to allow access to the NASA GESDISC Data archive. Additionally, to store password credentials for automatic data retrievals, initialize a .netrc file directed to urs.earthdata.nasa.gov and an empy .urs_cookies file (https://wiki.earthdata.nasa.gov/display/HDD/Wget+with+URS+Authentication#WgetwithURSAuthentication-Step-by-stepguide). 

## Acknowledgments
#### I would like to acknowledge Richard Cullather for providing instructions on using Wget and Jan Lenaerts for providing starter scripts on processing Wget output into netCDF files. 

## Data come from the following streams: 
##### Precipitation: "MERRA-2 tavg ... 1 Hourly, Time Averaged, Single-Level, Assimilation, Vertically Integrated Diagnostics... (tavg1_2d_int_Nx)" PRECCU, PRECLSC, PRECSNO. 

##### Radiation: "MERRA-2 tavg ... 1 Hourly, Time Averaged, Single-Level, Assimilation, Radiation Diagnostics... (tavg1_2d_rad_Nx)" LWGAB, LWGEM, LWGNT, SWGDN, SWGNT. 

##### Surface: "MERRA-2 tavg ... 1 Hourly, Time Averaged, Single-Level, Assimilation, Single-Level Diagnostics ... (tavg1_2d_slv_Nx)" PS, QV2M, T2M, TS, U10M, V10M.


