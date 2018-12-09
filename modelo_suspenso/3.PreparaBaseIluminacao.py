import pandas as pd
import pickle

iluminacao = pd.read_csv(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\ilume-limpa.csv', sep=',')
with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\iluminacao.pickle', 'wb') as handle:
    pickle.dump(iluminacao, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\PREFEITURA_SP\iluminacao.pickle', 'rb') as handle:
    iluminacao = pickle.load(handle)

print(len(iluminacao))
iluminacao = iluminacao.sample(1000)
print(len(iluminacao))
print(iluminacao[:10])