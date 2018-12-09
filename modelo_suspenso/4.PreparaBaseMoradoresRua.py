import pandas as pd
import pickle

OBT14 = pd.read_excel(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\OBT_2014.xlsx')
with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\OBT14.pickle', 'wb') as handle:
    pickle.dump(OBT14, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\OBT14.pickle', 'rb') as handle:
    OBT14 = pickle.load(handle)

print(len(OBT14))
OBT14 = OBT14.sample(1000)
print(len(OBT14))
print(OBT14[:10])