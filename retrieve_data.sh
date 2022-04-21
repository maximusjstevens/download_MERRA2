#!/bin/bash

# Option to specify where to save the MERRA-2 files (MS)
# dpth='/Volumes/Samsung_T1/MTEST' #save in present directory
dpth='/Users/cdsteve2/RCMdata/M2'
# dpth='/PATH/TO/DIRECTORY' #e.g. if you want to put on an externa drive

# This script will retrieve data by executing wget URLs. 
cd surface
rm MERRA2*
rm tmp*
wget -P $dpth --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies --content-disposition -i wget_surface.sh
cd ..

cd radiation
rm MERRA2*
rm tmp*
wget -P $dpth --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies --content-disposition -i wget_radiation.sh
cd ..

cd precip
rm MERRA2*
rm tmp*
wget -P $dpth --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies --content-disposition -i wget_precip.sh
cd ..

cd evap
rm MERRA2*
rm tmp*
wget -P $dpth --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies --content-disposition -i wget_evap.sh
cd ..
