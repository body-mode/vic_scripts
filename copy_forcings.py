import os
import shutil

#cd github folder

from colo_r_basins import latlon_x as latlon_d

#cd forcing folder

def basin_forcings(basin):
	if basin in os.listdir('.'):
		pass
	else:
		os.mkdir('C:/cygwin64/home/global/VIC/input/vic/forcing/historical/updated/master/%s' % (basin))
	for i in latlon_d[basin]:
		for fn in os.listdir('.'):
#			if fn == 'fluxes_%s_%s' % (i[0], i[1]):
#			if fn == 'snow_%s_%s' % (i[0], i[1]):
			if fn == 'data_%s_%s' % (i[0], i[1]):
				print fn
				shutil.copyfile(fn, 'C:/cygwin64/home/global/VIC/input/vic/forcing/historical/updated/master/%s/%s' % (basin, fn))