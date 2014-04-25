import os
import shutil

latlon_dict = {'test' : [(3,4), (4,3), (2,7)]}

def basin_forcings(basin):
	if basin in os.listdir('.'):
		pass
	else:
		os.mkdir('./%s' % (basin))
	for i in latlon_dict[basin]:
		for fn in os.listdir('.'):
			if fn == 'data_%s_%s' % (i[0], i[1]):
				print fn
				shutil.copyfile(fn, 'C:/Users/chesterlab/Desktop/EHE-days/%s/%s' % (basin, fn))
		