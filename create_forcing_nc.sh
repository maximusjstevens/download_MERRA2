#!/bin/csh -fx

# (MS) I Not sure about all of this front matter (ml, export commands)
# this script runs on my macbook with it commented out. It looks like they
# are environment specific; could be generalized?

# ml gcc/6.1.0
# ml openmpi/2.0.1
# ml proj
# ml netcdf 

# export LDFLAGS='-L/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/lib/ -L/projects/nawe3645/usr/lib/'
# export CPPFLAGS='-I/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/include -I/projects/nawe3645/usr/include/'
# ./configure --prefix /projects/nawe3645/usr/ --with-netcdf=/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/ --enable-netcdf4

# This script processes wget outout files and processes them into netcdf files with cdo. 
# it could be generalized to process whatever (all) variables that were downloaded,
# if they differ from those listed below (i.e. what are needed for SNOWPACK runs)
set varlist = ( LWGAB LWGEM LWGNT SWGDN SWGNT PS QV2M T2M TS U10M V10M H500 PRECCU PRECLS PRECSN EVAP )

set year = $1
set year_end = $2

while ( $year < $year_end + 1 )
foreach vr ( $varlist )
# set pp = "/scratch/summit/erke2265/download_MERRA2/"
set pp = "$3/" #use the same datapath as speficied in download_MERRA2.sh
if ( $vr == "FRSEAICE" ) then
	#set pp = "${pp}seaice"
	cd ${pp}seaice
else
	if ( $vr == "SNOWDP_GL") then
		set pp = "${pp}snowh"
	else
		if ($vr == "EVAP") then
			set pp = "${pp}evap"
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
endif			
				
set nr = 100000

rm -f tmp*nc
rm -f tmp
cd "${pp}"

foreach fil (MERRA2*${year}*)
	echo "$nr"
	cp "$fil" tmp	
	cdo selvar,$vr tmp tmp$nr.nc
	# User may need to point at cdo if it is not in $PATH already, e.g.:
	# /projects/nawe3645/usr/bin/cdo selvar,$vr tmp tmp$nr.nc
	@ nr = $nr + 1
	end

set tmplist = ( `ls tmp*nc | sort` )
cdo cat $tmplist ../nc_files/$vr"_hourly_"$year".nc"
# /projects/nawe3645/usr/bin/cdo cat $tmplist ../nc_files/$vr"_hourly_"$year".nc"
end
@ year = $year + 1
# endif #(MS) I think this was an extra endif?

end

# (MS) remove the tmp files associated with the last variable in varlist 
# (was not done previously due to loop structure)
rm -f tmp
rm -f tmp*nc



