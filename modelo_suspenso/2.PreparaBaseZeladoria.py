import pandas as pd
import pickle

zeladoria1701 = pd.read_excel(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\dados-do-sp156---1-sem-2017.xlsx')
with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\dados-do-sp156---1-sem-2017.pickle', 'wb') as handle:
    pickle.dump(zeladoria1701, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\dados-do-sp156---1-sem-2017.pickle', 'rb') as handle:
    zeladoria1701 = pickle.load(handle)

print(len(zeladoria1701))
zeladoria1701 = zeladoria1701.sample(1000)
print(len(zeladoria1701))
print(zeladoria1701[:10])