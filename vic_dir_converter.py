import numpy as np
import pandas as pd

d = {1:3, 2:4, 4:5, 8:6, 16:7, 32:8, 64:1, 128:2, -9999:0, 0:0}

line_li = []
new_li = []

df = pd.DataFrame()

f = open('lee_f_dir_8d_ascii.txt', 'r')
tempfile = open('lee_f_dir_8d_ascii_write.txt', 'w')

fwf = pd.read_table('lee_f_dir_8d_ascii.txt', sep=' ', skiprows=6, header=None)
#del fwf[len(fwf.columns)-1]

for i in range(len(fwf)):
    line_li.append(list(fwf.ix[i]))

for j in line_li:
	templi = []
	for k in j:
		if k in d.keys():
			templi.append(d[k])
		else:
			continue
	new_li.append(templi)

new_s = []

for i in new_li:
	new_s.append(pd.Series(i))
	
df = df.append(new_s, ignore_index=True)

dfwrite = df.to_csv('dfwrite.txt', sep=' ', header=False, index=False)
dfread = open('dfwrite.txt', 'r')

head = f.readlines()[:6]

for i in head:
	tempfile.write(i)

for i in dfread.readlines():
	tempfile.write(i)

f.close()
tempfile.close()