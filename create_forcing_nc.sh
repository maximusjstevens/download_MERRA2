#!/bin/csh -fx

# This script processes wget outout files and processes them into netcdf files with cdo. 

set varlist = ( LWGAB LWGEM LWGNT SWGDN SWGNT PS QV2M T2M TS U10M V10M PRECCU PRECLS PRECSN )

set year = 1980
set year_end = 1981

while ( $year < $year_end + 1 )
foreach vr ( $varlist )
set pp = "/Users/eric/Ice sheets & Climate Dropbox/Eric Keenan/download_MERRA2/"
if ( $vr == "FRSEAICE" ) then
	set pp = "${pp}seaice"
else
	if ( $vr == "SNOWDP_GL") then
		set pp = "${pp}snowh"
	else
		if ( $vr == "PRECCU" || $vr == "PRECLS" || $vr == "PRECSN" ) then
			set pp = "${pp}precip"
		else
			if ( $vr == "LWGAB" || $vr == "LWGEM" || $vr == "LWGNT" || $vr == "SWGDN" || $vr == "SWGNT" ) then
				set pp = "${pp}radiation"
			else
				set pp = "${pp}surface"
			endif
		endif
	endif
endif			
				
set nr = 10000

rm -f tmp*nc
rm -f tmp
# foreach fil ( $pp/HTTP*$year*nc4* )
cd "${pp}"
foreach fil (HTTP*$year*)
#foreach fil ($pp/HTTP_services.cgi?FILENAME=%2Fdata%2FMERRA2%2FM2T1NXSLV.5.12.4%2F1995%2F01%2FMERRA2_200.tavg1_2d_slv_Nx.19950101.nc4\&FORMAT=bmM0Lw\&BBOX=-90,-180,-40,180\&LABEL=MERRA2_200.tavg1_2d_slv_Nx.19950101.SUB.nc4\&SHORTNAME=M2T1NXSLV\&SERVICE=SUBSE)
	cp $fil tmp
	cdo selvar,$vr tmp tmp$nr.nc
	# cdo selvar,$vr $fil tmp$nr.nc
	@ nr = $nr + 1
  	end
# set tmplist = { `ls tmp*nc | sort` }
set tmplist = ( `ls tmp*nc | sort` )
cdo cat $tmplist ../nc_files/$vr"_hourly_"$year".nc"
end
@ year = $year + 1
end


