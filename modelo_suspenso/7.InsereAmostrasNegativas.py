import pandas as pd
import numpy as np
import pickle
pd.set_option('display.max_columns', 1000)

with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_bo1.pickle', 'rb') as handle:
    base_bo1 = pickle.load(handle)


with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\dados-do-sp156---1-sem-2017.pickle', 'rb') as handle:
    zeladoria1701 = pickle.load(handle)

zeladoria1701.Filtro = zeladoria1701.Latitude.apply(lambda x: 1 if str(x).strip() != '' else 0)
zeladoria1701 = zeladoria1701[zeladoria1701.Filtro == 1]

periodos = base_bo1.groupby('PERIDOOCORRENCIA').LOGRADOURO.count().reset_index(name='QTDOCORRENCIA').drop('QTDOCORRENCIA', axis=1)

zeladoria1701inflada = pd.merge(zeladoria1701.assign(key=0), periodos.assign(key=0), on='key').drop('key', axis=1)
n_bo1 = len(base_bo1)

features = ['Logradouro','Latitude','Longitude','PERIDOOCORRENCIA']
base_bo0 = zeladoria1701inflada[features].sample(n_bo1)
base_bo0.columns = [c.upper() for c in features]

base_bo1['TARGET'] = 1
base_bo0['TARGET'] = 0

base_all = pd.concat([base_bo1.reset_index(), base_bo0.reset_index()], axis=0)

with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_bo0.pickle', 'wb') as handle:
    pickle.dump(base_bo0, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_all.pickle', 'wb') as handle:
    pickle.dump(base_all, handle, protocol=pickle.HIGHEST_PROTOCOL)