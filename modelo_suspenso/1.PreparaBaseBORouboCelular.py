import pandas as pd
import pickle
import os

dir_data = r'C:\Users\usuario_itau\Desktop\ITAU\CidadeSegura\Base 08 - Transparência Dados BO\BOs2017e2018\Roubo Celular'

base = pd.DataFrame()
n = 0
for subdir, dirs, files in os.walk(dir_data):
    for file in files:

        if file[:12] != 'DadosBO_2017' or file.__contains__('pickle'):
            continue

        try:
            base = pd.read_excel(os.path.join(subdir, file)) if n == 0 else pd.concat([base,pd.read_excel(os.path.join(subdir, file))])
            n+=1
            print(file, len(base))
        except:
            print(file)
            pass

        n += 1

with open(r'C:\Users\usuario_itau\Desktop\ITAU\CidadeSegura\Base 08 - Transparência Dados BO\BOs2017e2018\base_roubo_celular.pickle', 'wb') as handle:
    pickle.dump(base, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(r'C:\Users\usuario_itau\Desktop\ITAU\CidadeSegura\Base 08 - Transparência Dados BO\BOs2017e2018\base_roubo_celular.pickle', 'rb') as handle:
    base = pickle.load(handle)

print(len(base))
base = base.sample(1000)
print(len(base))
print(base[:10])