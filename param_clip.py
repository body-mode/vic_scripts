import pandas as pd
import numpy as np
import pickle
import os
import ast 

##################################
#STORE REGIONAL SOIL PARAMS
##################################

#cd soil params directory

d = {}

for fn in os.listdir('.'):
	print fn
	f = pd.read_table(fn, sep=' ')
	f.columns = [range(len(f.columns))]
	d.update({fn : f})


r_latlon_d = {}

for i, v in d.items():
	v['latlon'] = zip(v[2], v[3])
	r_latlon_d.update({i[10:] : v['latlon']})

out = open("region_latlon.p", "wb")
pickle.dump(r_latlon_d, out)
out.close()

#LOAD LATLON PICKLE

r_latlon = pickle.load( open( "./region_latlon.p", "rb"))
		
#######################################
#STORE SOIL, VEG, SNOWBANDS as HDF5
#######################################

master_param = pd.HDFStore('master_param.h5')



#SOIL


#cd soil region dir

soil_d = {}

for fn in os.listdir('.'):
	print fn
	f = pd.read_table(fn, sep=' ')
	f.columns = [range(len(f.columns))]
	soil_d.update({fn : f})

soil = pd.concat([x for x in soil_d.values()])



#VEG

#cd veg region dir

fn_li = [i for i in os.listdir('.')]

with open('master_veg', 'w') as outfile:
    for fname in fn_li:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
				

			
#SNOWBANDS

#cd snowband region dir

snow_d = {}

for fn in os.listdir('.'):
	print fn
	f = pd.read_table(fn, sep=' ')
	f.columns = [range(len(f.columns))]
	snow_d.update({fn : f})

snow = pd.concat([x for x in snow_d.values()])


#HDFSTORE


master_param['soil'] = soil
master_param['veg'] = veg
master_param['snow'] = snow

#GRIDCELL

#master_param = pd.HDFStore('master_param.h5')

soil = master_param.soil

soil['latlon'] = zip(soil[2], soil[3])
soil['st_latlon'] = soil['latlon'].astype(str)
soil = soil.set_index(soil['st_latlon'])
gridcel = soil[1]


master_param['gridcel'] = gridcel

##########################################
#CLIP PREPARATION
##########################################

#cd project_files

import pandas as pd
import numpy as np
import pickle
import os
import ast 

from colo_r_basins import latlon_x as latlon_d
master_param = pd.HDFStore('master_param.h5')

##########################################
#CLIP REGIONAL SOIL PARAMS TO TARGET BASIN
##########################################

def clip_soil(basin):

	master_param.open()
	soil = master_param.soil
	soil = soil.ix[soil[4] > 0.0]
	master_param.close()
	soil['latlon'] = zip(soil[2], soil[3])
	soil['st_latlon'] = soil['latlon'].astype(str)
	soil = soil.set_index(soil['st_latlon'])
	del soil['latlon']
	del soil['st_latlon']
	latlon_s = [str(i) for i in latlon_d[basin]]
	soilclip = soil.ix[latlon_s]
	soilclip = soilclip.dropna(axis=0, subset=[0])
	soilclip = soilclip.dropna(axis=1)
	soilclip = soilclip.drop_duplicates(cols=1)
	soilclip[0] = soilclip[0].astype(int)
#	print soilclip
	print set(soilclip[0])
	if not os.path.exists('soil'):
		os.mkdir('soil')
	else:
		pass
	soilclip.to_csv('./soil/soil_%s' % (basin), sep = ' ', header=False, index=False)

############################################
#CLIP VEG PARAMS TO TARGET BASIN
############################################



veg_d = {}

def make_veg_d():

	f = open('master_veg', 'r')
	rf = f.readlines()[:]
	f.close()
	
	f = open('master_veg', 'r')
	
	for i, line in enumerate(f):
		if line[0] in ['1','2','3','4','5','6','7','8','9']:
			par_l = line.split()
			gridcel = par_l[0]
			nveg = ast.literal_eval(par_l[1])
#			print gridcel, type(gridcel)
#			print nveg, type(nveg)
#			print i
			nlines = [j for j in rf[i+1: i + nveg*2 + 1]]
			veg_d.update({gridcel : (nveg, nlines)})

			
def clip_veg(basin):
	master_param.open()
	gridcel = master_param.gridcel
	master_param.close()
	latlon_s = [str(i) for i in latlon_d[basin]]
	gridcel_s = gridcel[latlon_s]
	if not os.path.exists('veg'):
		os.mkdir('veg')
	else:
		pass
	newveg = open('./veg/veg_%s' % (basin), 'w')
#	print gridcel_s
	for i in gridcel_s.values:
		i = i.astype(str)
		newveg.write("%s %s\n" % (i, veg_d[i][0]))
		for j in veg_d[i][1]:
			newveg.write("%s" % (j))
			


##############################################			
#CLIP SNOWBANDS TO TARGET BASIN
##############################################


def clip_snow(basin):

	master_param.open()
	snow = master_param.snow
	gridcel = master_param.gridcel
	master_param.close()
	snow = snow.set_index(snow[0])
	latlon_s = [str(i) for i in latlon_d[basin]]
#	print latlon_s
	gridcel_s = gridcel[latlon_s]
#	print gridcel_s
	snowclip = snow.ix[gridcel_s]
#	print snowclip.tail()
	snowclip = snowclip.drop_duplicates(cols=0)
	snowclip = snowclip.dropna(axis=0, subset=[0])
	snowclip = snowclip.dropna(axis=1)
#	for i in snowclip.columns:
#		snowclip[i] = np.round(snowclip[i], 4)
#	print snowclip
#	print len(snowclip.index)
#	print len(set(list(snowclip.index)))
	if not os.path.exists('snowbands'):
		os.mkdir('snowbands')
	else:
		pass
	snowclip.to_csv('./snowbands/snowbands_%s' % (basin), sep = ' ', header=False, index=False)

##################################################
CONVERT EOL TO UNIX
##################################################

import os
import string

def convert_line_endings(temp, mode):
        #modes:  0 - Unix, 1 - Mac, 2 - DOS
        if mode == 0:
                temp = string.replace(temp, '\r\n', '\n')
                temp = string.replace(temp, '\r', '\n')
        elif mode == 1:
                temp = string.replace(temp, '\r\n', '\r')
                temp = string.replace(temp, '\n', '\r')
        elif mode == 2:
                import re
                temp = re.sub("\r(?!\n)|(?<!\r)\n", "\r\n", temp)
        return temp
		
def convert_dir():
	for fn in os.listdir('.'):
		print fn
		fr = open(fn, 'r')
		fc = [i for i in fr.readlines()]
		fr.close()
		fw = open(fn, 'w')
		for i in fc:
			fw.write(convert_line_endings(i, 0))

##################################################
#APPLY CLIP
##################################################

for basin in latlon_d.keys():
	clip_soil(basin)

make_veg_d()

for basin in latlon_d.keys():
	clip_veg(basin)

for basin in latlon_d.keys():
	clip_snow(basin)