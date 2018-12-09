import pandas as pd
import numpy as np
import pickle
pd.set_option('display.max_columns', 1000)

import math


with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.pickle', 'rb') as handle:
    base_all = pickle.load(handle)

with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\OBT14.pickle', 'rb') as handle:
    obt14 = pickle.load(handle)


obt14 = obt14[['ID', 'LATITUDE', 'LONGITUDE']]

base_all.LATITUDE = base_all.LATITUDE.apply(lambda x: float(str(x).replace(',','.')))
obt14.LATITUDE = obt14.LATITUDE.apply(lambda x: float(str(x).replace(',','.')))

base_all.LONGITUDE = base_all.LONGITUDE.apply(lambda x: float(str(x).replace(',','.')))
obt14.LONGITUDE = obt14.LONGITUDE.apply(lambda x: float(str(x).replace(',','.')))

#crosstable = pd.merge(base_all.assign(key=0), zeladoria1701.assign(key=0), on='key', suffixes=('_ini','_fim')).drop('key', axis=1)

def DistanciaKm(lat_ini, lat_fim, lon_ini, lon_fim, k):
    try:
        lat1 = lat_ini
        lat2 = float(lat_fim)
        lon1 = lon_ini
        lon2 = float(lon_fim)

        return (6371 * math.acos(math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon2) - math.radians(lon1)) + math.sin(math.radians(lat1)) * math.sin(math.radians(lat2))))
    except Exception as ex:
        print(lat_ini, lat_fim, lon_ini, lon_fim, k, ex)
        return(999)

i_columns = base_all.columns
j_columns = obt14.columns
list_result = []
k = 1

print(i_columns)
print(j_columns)

for i in base_all.values.tolist():
    l = 1
    for j in obt14.values.tolist():
        dist = DistanciaKm(i[2], j[1], i[3], j[2], str(k)+'-'+str(l))
        if dist < 1:
            list_result.append(i + j)

        l+=1
    if k % 1000 == 0:
        print('Passo', k)
    k+=1


with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_morador_rua.pickle', 'wb') as handle:
    pickle.dump(list_result, handle, protocol=pickle.HIGHEST_PROTOCOL)

#crosstable['dist'] = crosstable.apply(lambda row: DistanciaKm(row['lat1'], row['lat2'], row['lon1'], row['lon2']), axis=1)

#base_bo0 = zeladoria1701inflada[features].sample(n_bo1)
#base_bo0.columns = [c.upper() for c in features]

#base_all = pd.concat([base_bo1.reset_index(), base_bo0.reset_index()], axis=0)

#with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_bo0.pickle', 'wb') as handle:
#    pickle.dump(base_bo0, handle, protocol=pickle.HIGHEST_PROTOCOL)

#with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.pickle', 'wb') as handle:
#    pickle.dump(base_all, handle, protocol=pickle.HIGHEST_PROTOCOL)