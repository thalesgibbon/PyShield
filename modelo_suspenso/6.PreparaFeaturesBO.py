import pandas as pd
import pickle

with open(r'C:\Users\usuario_itau\Desktop\ITAU\CidadeSegura\Base 08 - Transparência Dados BO\BOs2017e2018\base_roubo_celular.pickle', 'rb') as handle:
    base_bo_roubo_celular = pickle.load(handle)


print(len(base_bo_roubo_celular))
base_bo_roubo_celular = base_bo_roubo_celular.sample(1000)
base_bo_roubo_celular = base_bo_roubo_celular[base_bo_roubo_celular['CIDADE']=='S.PAULO']
print(len(base_bo_roubo_celular))
print(base_bo_roubo_celular[:10])
print(base_bo_roubo_celular.columns)

features = ['LOGRADOURO','LATITUDE','LONGITUDE','PERIDOOCORRENCIA']

base_bo1 = base_bo_roubo_celular[features]

with open(r'C:\Users\usuario_itau\Desktop\PRE_BASES\base_bo1.pickle', 'wb') as handle:
    pickle.dump(base_bo1, handle, protocol=pickle.HIGHEST_PROTOCOL)

