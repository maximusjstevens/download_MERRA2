#!/bin/bash

# This script will retrieve data by executing wget URLs. 
cd surface
rm HTTP*
rm tmp*
wget -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_surface.sh

cd ../radiation
rm HTTP*
rm tmp*
wget -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_radiation.sh

cd ../precip
rm HTTP*
rm tmp*
wget -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_precip.sh

cd ../evap
rm HTTP*
rm tmp*
wget -nc --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -i wget_evap.sh
