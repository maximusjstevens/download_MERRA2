#!/bin/bash

# This script will retrieve data by executing wget URLs. 
cd surface
rm MERRA2*
rm tmp*
wget -c -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_surface.sh

cd ../radiation
rm MERRA2*
rm tmp*
wget -c -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_radiation.sh

cd ../precip
rm MERRA2*
rm tmp*
wget -c -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_precip.sh

cd ../evap
rm MERRA2*
rm tmp*
wget -c -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_evap.sh
