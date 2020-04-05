#!/bin/csh -fx
ml gcc/6.1.0
ml openmpi/2.0.1
ml proj
ml netcdf 

export LDFLAGS='-L/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/lib/ -L/projects/nawe3645/usr/lib/'
export CPPFLAGS='-I/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/include -I/projects/nawe3645/usr/include/'
./configure --prefix /projects/nawe3645/usr/ --with-netcdf=/curc/sw/netcdf/4.4.1.1/gcc/6.1.0/ --enable-netcdf4

# This script processes wget outout files and processes them into netcdf files with cdo. 
set varlist = ( LWGAB LWGEM LWGNT SWGDN SWGNT PS QV2M T2M TS U10M V10M H500 PRECCU PRECLS PRECSN EVAP )

set year = $1
set year_end = $2

while ( $year < $year_end + 1 )
foreach vr ( $varlist )
set pp = "/scratch/summit/erke2265/download_MERRA2/"
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
	/projects/nawe3645/usr/bin/cdo selvar,$vr tmp tmp$nr.nc
	@ nr = $nr + 1
	end

set tmplist = ( `ls tmp*nc | sort` )
/projects/nawe3645/usr/bin/cdo cat $tmplist ../nc_files/$vr"_hourly_"$year".nc"
end
@ year = $year + 1
endif

end




