import pandas as pd
import numpy as np
import pickle
pd.set_option('display.max_columns', 1000)

with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.pickle', 'rb') as handle:
    base_all = pickle.load(handle)
with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_zelatoria.pickle', 'rb') as handle:
    l_zelatoria = pickle.load(handle)
with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_morador_rua.pickle', 'rb') as handle:
    l_morador_rua = pickle.load(handle)
with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_distpol.pickle', 'rb') as handle:
    l_distol = pickle.load(handle)

#print(base_all.columns + ['SERVICO', 'STATUS', 'LATITUDE', 'LONGITUDE'])
print(l_zelatoria[10])
cross_zelatoria = pd.DataFrame(l_zelatoria, columns=list(base_all.columns) + ['SERVICO', 'STATUS', 'LATITUDE', 'LONGITUDE'])
cross_morador_rua = pd.DataFrame(l_morador_rua, columns=list(base_all.columns) +['ID', 'LATITUDE', 'LONGITUDE'])
cross_distpol = pd.DataFrame(l_distol, columns=list(base_all.columns) + ['LATITUDE', 'LONGITUDE'])

base_all.to_csv(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.csv')
cross_zelatoria.to_csv(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_zelatoria.csv')
cross_morador_rua.to_csv(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_morador_rua.csv')
cross_distpol.to_csv(r'C:\Users\usuario_itau\Desktop\PRE_BASES\cross_distpol.csv')


#crosstable['dist'] = crosstable.apply(lambda row: DistanciaKm(row['lat1'], row['lat2'], row['lon1'], row['lon2']), axis=1)

#base_bo0 = zeladoria1701inflada[features].sample(n_bo1)
#base_bo0.columns = [c.upper() for c in features]

#base_all = pd.concat([base_bo1.reset_index(), base_bo0.reset_index()], axis=0)

#with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_bo0.pickle', 'wb') as handle:
#    pickle.dump(base_bo0, handle, protocol=pickle.HIGHEST_PROTOCOL)

#with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.pickle', 'wb') as handle:
#    pickle.dump(base_all, handle, protocol=pickle.HIGHEST_PROTOCOL)