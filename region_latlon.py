#cd soil params directory

import pandas as pd
import numpy as np
import pickle

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
	
pickle.dump(r_latlon_d, open("region_latlon.p", "wb"))

#r_latlon = pickle.load( open( "region_latlon.p", "rb"))