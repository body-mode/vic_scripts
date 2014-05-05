import numpy as np
import pandas as pd
from datetime import date
import ast

nat_int = pd.read_csv('LC_natural_mo_flow.csv')
nat_int = nat_int.dropna()
nat_int['datesplit'] = [i.split('/') for i in nat_int['date']]
nat_int['realdate'] = [date(ast.literal_eval(i[2]), ast.literal_eval(i[0]), ast.literal_eval(i[1])) for i in nat_int['datesplit']]
del nat_int['date']
nat_int['date'] = nat_int['realdate']
del nat_int['realdate']
del nat_int['datesplit']

nat_tot = pd.read_csv('LC_natural_mo_flow_tot.csv')
nat_tot = nat_tot.dropna()
nat_tot['datesplit'] = [i.split('/') for i in nat_tot['date']]
nat_tot['realdate'] = [date(ast.literal_eval(i[2]), ast.literal_eval(i[0]), ast.literal_eval(i[1])) for i in nat_tot['datesplit']]
del nat_tot['date']
nat_tot['date'] = nat_tot['realdate']
del nat_tot['realdate']
del nat_tot['datesplit']



lees_f = pd.read_table('./hist/lees_.month', header=None, sep=' ', skipinitialspace=True)
lees_f = lees_f.dropna(axis=1)
lees_f.columns = ['year', 'month', 'cfs']
lees_f2 = pd.read_table('./a1b/lees_.month', header=None, sep=' ', skipinitialspace=True)
lees_f2 = lees_f2.dropna(axis=1)
lees_f2.columns = ['year', 'month', 'cfs']
lees_fc = pd.concat([lees_f, lees_f2])
lees_fc = lees_fc.reset_index()
del lees_fc['index']
lees_fc['day'] = 28
lees_fc['date'] = zip(lees_fc['year'], lees_fc['month'], lees_fc['day'])
lees_fc['date'] = [date(i[0], i[1], i[2]) for i in lees_fc['date']]

plot(lees_fc.date, lees_fc.cfs)
plot(nat_int['date'], nat_int['lees_f'])




billw = pd.read_table('./hist/billw.month', header=None, sep=' ', skipinitialspace=True)
billw = billw.dropna(axis=1)
billw.columns = ['year', 'month', 'cfs']
billw2 = pd.read_table('./a1b/billw.month', header=None, sep=' ', skipinitialspace=True)
billw2 = billw2.dropna(axis=1)
billw2.columns = ['year', 'month', 'cfs']
billwc = pd.concat([billw, billw2])
billwc = billwc.reset_index()
del billwc['index']
billwc['day'] = 28
billwc['date'] = zip(billwc['year'], billwc['month'], billwc['day'])
billwc['date'] = [date(i[0], i[1], i[2]) for i in billwc['date']]

plot(billwc.date, billwc.cfs)
plot(nat_int['date'], nat_int['billw'])




davis = pd.read_table('./hist/davis.month', header=None, sep=' ', skipinitialspace=True)
davis = davis.dropna(axis=1)
davis.columns = ['year', 'month', 'cfs']
davis2 = pd.read_table('./a1b/davis.month', header=None, sep=' ', skipinitialspace=True)
davis2 = davis2.dropna(axis=1)
davis2.columns = ['year', 'month', 'cfs']
davisc = pd.concat([davis, davis2])
davisc = davisc.reset_index()
del davisc['index']
davisc['day'] = 28
davisc['date'] = zip(davisc['year'], davisc['month'], davisc['day'])
davisc['date'] = [date(i[0], i[1], i[2]) for i in davisc['date']]

plot(davisc.date, davisc.cfs)
plot(nat_int['date'], nat_int['davis'])




gc = pd.read_table('./hist/gc.month', header=None, sep=' ', skipinitialspace=True)
gc = gc.dropna(axis=1)
gc.columns = ['year', 'month', 'cfs']
gc2 = pd.read_table('./a1b/gc.month', header=None, sep=' ', skipinitialspace=True)
gc2 = gc2.dropna(axis=1)
gc2.columns = ['year', 'month', 'cfs']
gcc = pd.concat([gc, gc2])
gcc = gcc.reset_index()
del gcc['index']
gcc['day'] = 28
gcc['date'] = zip(gcc['year'], gcc['month'], gcc['day'])
gcc['date'] = [date(i[0], i[1], i[2]) for i in gcc['date']]

plot(gcc.date, gcc.cfs)
plot(nat_int['date'], nat_int['gc'])




hoover = pd.read_table('./hist/hoove.month', header=None, sep=' ', skipinitialspace=True)
hoover = hoover.dropna(axis=1)
hoover.columns = ['year', 'month', 'cfs']
hoover2 = pd.read_table('./a1b/hoove.month', header=None, sep=' ', skipinitialspace=True)
hoover2 = hoover2.dropna(axis=1)
hoover2.columns = ['year', 'month', 'cfs']
hooverc = pd.concat([hoover, hoover2])
hooverc = hooverc.reset_index()
del hooverc['index']
hooverc['day'] = 28
hooverc['date'] = zip(hooverc['year'], hooverc['month'], hooverc['day'])
hooverc['date'] = [date(i[0], i[1], i[2]) for i in hooverc['date']]

plot(hooverc.date, hooverc.cfs)
plot(nat_int['date'], nat_int['hoover'])




little_col = pd.read_table('./hist/littl.month', header=None, sep=' ', skipinitialspace=True)
little_col = little_col.dropna(axis=1)
little_col.columns = ['year', 'month', 'cfs']
little_col2 = pd.read_table('./a1b/littl.month', header=None, sep=' ', skipinitialspace=True)
little_col2 = little_col2.dropna(axis=1)
little_col2.columns = ['year', 'month', 'cfs']
little_colc = pd.concat([little_col, little_col2])
little_colc = little_colc.reset_index()
del little_colc['index']
little_colc['day'] = 28
little_colc['date'] = zip(little_colc['year'], little_colc['month'], little_colc['day'])
little_colc['date'] = [date(i[0], i[1], i[2]) for i in little_colc['date']]

plot(little_colc.date, little_colc.cfs)
plot(nat_int['date'], nat_int['little_col'])




imperial = pd.read_table('./hist/imper.month', header=None, sep=' ', skipinitialspace=True)
imperial = imperial.dropna(axis=1)
imperial.columns = ['year', 'month', 'cfs']
imperial2 = pd.read_table('./a1b/imper.month', header=None, sep=' ', skipinitialspace=True)
imperial2 = imperial2.dropna(axis=1)
imperial2.columns = ['year', 'month', 'cfs']
imperialc = pd.concat([imperial, imperial2])
imperialc = imperialc.reset_index()
del imperialc['index']
imperialc['day'] = 28
imperialc['date'] = zip(imperialc['year'], imperialc['month'], imperialc['day'])
imperialc['date'] = [date(i[0], i[1], i[2]) for i in imperialc['date']]

plot(imperialc.date, imperialc.cfs)
plot(nat_int['date'], nat_int['imperial'])




paria = pd.read_table('./hist/paria.month', header=None, sep=' ', skipinitialspace=True)
paria = paria.dropna(axis=1)
paria.columns = ['year', 'month', 'cfs']
paria2 = pd.read_table('./a1b/paria.month', header=None, sep=' ', skipinitialspace=True)
paria2 = paria2.dropna(axis=1)
paria2.columns = ['year', 'month', 'cfs']
pariac = pd.concat([paria, paria2])
pariac = pariac.reset_index()
del pariac['index']
pariac['day'] = 28
pariac['date'] = zip(pariac['year'], pariac['month'], pariac['day'])
pariac['date'] = [date(i[0], i[1], i[2]) for i in pariac['date']]
paria['day'] = 28
paria['date'] = zip(paria['year'], paria['month'], paria['day'])
paria['date'] = [date(i[0], i[1], i[2]) for i in paria['date']]

pariac_line, = plot(pariac.date, pariac.cfs)
paria_int_line, = plot(nat_int['date'], nat_int['paria'])
title('Instantaneous Gains at Paria River, Near Glen Canyon')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((pariac_line, paria_int_line), ('modeled', 'historical'))

paria_line, = plot(paria.date, paria.cfs)
paria_int_line, = plot(nat_int['date'], nat_int['paria'])
title('Instantaneous Gains at Paria River, Near Glen Canyon')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((paria_line, paria_int_line), ('modeled', 'historical'))

parker = pd.read_table('./hist/parke.month', header=None, sep=' ', skipinitialspace=True)
parker = parker.dropna(axis=1)
parker.columns = ['year', 'month', 'cfs']
parker2 = pd.read_table('./a1b/parke.month', header=None, sep=' ', skipinitialspace=True)
parker2 = parker2.dropna(axis=1)
parker2.columns = ['year', 'month', 'cfs']
parkerc = pd.concat([parker, parker2])
parkerc = parkerc.reset_index()
del parkerc['index']
parkerc['day'] = 28
parkerc['date'] = zip(parkerc['year'], parkerc['month'], parkerc['day'])
parkerc['date'] = [date(i[0], i[1], i[2]) for i in parkerc['date']]

plot(parkerc.date, parkerc.cfs)
plot(nat_int['date'], nat_int['parker'])




virgin = pd.read_table('./hist/virgi.month', header=None, sep=' ', skipinitialspace=True)
virgin = virgin.dropna(axis=1)
virgin.columns = ['year', 'month', 'cfs']
virgin2 = pd.read_table('./a1b/virgi.month', header=None, sep=' ', skipinitialspace=True)
virgin2 = virgin2.dropna(axis=1)
virgin2.columns = ['year', 'month', 'cfs']
virginc = pd.concat([virgin, virgin2])
virginc = virginc.reset_index()
del virginc['index']
virginc['day'] = 28
virginc['date'] = zip(virginc['year'], virginc['month'], virginc['day'])
virginc['date'] = [date(i[0], i[1], i[2]) for i in virginc['date']]
virgin['day'] = 28
virgin['date'] = zip(virgin['year'], virgin['month'], virgin['day'])
virgin['date'] = [date(i[0], i[1], i[2]) for i in virgin['date']]

virginc_line, = plot(virginc.date, virginc.cfs)
virgin_int_line, = plot(nat_int['date'], nat_int['virgin'])
title('Instantaneous Gains at Virgin River, Near Hoover Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((virginc_line, virgin_int_line), ('modeled', 'historical'))

virgin_line, = plot(virgin.date, virgin.cfs)
virgin_int_line, = plot(nat_int['date'], nat_int['virgin'])
title('Instantaneous Gains at Virgin River, Near Hoover Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((virgin_line, virgin_int_line), ('modeled', 'historical'))

#model_master = pd.concat([lees_fc.date, lees_f.cfs, paria.cfs, little_col.cfs, gc.cfs, virgin.cfs, hoover.cfs, davis.cfs, parker.cfs, imperial.cfs], axis=1)
model_master = pd.concat([lees_fc.date, lees_fc.cfs, pariac.cfs, little_colc.cfs, gcc.cfs, virginc.cfs, hooverc.cfs, davisc.cfs, parkerc.cfs, imperialc.cfs], axis=1)
model_master.columns = ['date', 'lees_f', 'paria', 'little_col', 'gc', 'virgin', 'hoover', 'davis', 'parker', 'imperial']

model_cumsum = model_master
model_cumsum['gc'] = model_master['lees_f'] + model_master['paria'] + model_master['little_col']
model_cumsum['hoover'] = model_cumsum['gc'] + model_master['virgin'] + model_master['hoover']
model_cumsum['davis'] = model_cumsum['hoover'] + model_master['davis']
model_cumsum['parker'] = model_master['parker'] + model_cumsum['davis']
model_cumsum['imperial'] = model_cumsum['parker'] + model_master['imperial']


model_lees_f_line, = plot(model_cumsum.date, model_cumsum.gc)
hist_lees_f_line, = plot(nat_tot.date, nat_tot.gc)
title('Instantaneous Flow into Glen Canyon Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_lees_f_line, hist_lees_f_line), ('modeled', 'historical'))

model_gc_line, = plot(model_cumsum.date, model_cumsum.gc)
hist_gc_line, = plot(nat_tot.date, nat_tot.gc)
title('Instantaneous Flow into Grand Canyon')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_gc_line, hist_gc_line), ('modeled', 'historical'))

model_hoover_line, = plot(model_cumsum.date, model_cumsum.hoover)
hist_hoover_line, = plot(nat_tot.date, nat_tot.hoover)
title('Instantaneous Flow into Hoover Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_hoover_line, hist_hoover_line), ('modeled', 'historical'))

model_davis_line, = plot(model_cumsum.date, model_cumsum.davis)
hist_davis_line, = plot(nat_tot.date, nat_tot.davis)
title('Instantaneous Flow into Davis Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_davis_line, hist_davis_line), ('modeled', 'historical'))

model_parker_line, = plot(model_cumsum.date, model_cumsum.parker)
hist_parker_line, = plot(nat_tot.date, nat_tot.parker)
title('Instantaneous Flow into Parker Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_parker_line, hist_parker_line), ('modeled', 'historical'))

model_imperial_line, = plot(model_cumsum.date, model_cumsum.imperial)
hist_imperial_line, = plot(nat_tot.date, nat_tot.imperial)
title('Instantaneous Flow into Imperial Dam')
xlabel('Year')
ylabel('Discharge (cfs)')
leg = legend((model_imperial_line, hist_imperial_line), ('modeled', 'historical'))