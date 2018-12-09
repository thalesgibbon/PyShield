import pandas as pd
import pickle

distritos = pd.read_excel(r'C:\Users\usuario_itau\Desktop\CRIADAS\Distritos_de_Policia.xlsx')
with open(r'C:\Users\usuario_itau\Desktop\CRIADAS\Distritos_de_Policia.pickle', 'wb') as handle:
    pickle.dump(distritos, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\CRIADAS\Distritos_de_Policia.pickle', 'rb') as handle:
    distritos = pickle.load(handle)

print(len(distritos))
print(distritos[:10])