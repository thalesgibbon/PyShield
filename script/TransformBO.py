from __future__ import unicode_literals
import os
import pandas as pd
from __config__ import path_data
import numpy as np


path = path_data + r"\extract\BOs"


class TransformBO(object):
    def __init__(self):
        self.cols = [ 'DATAOCORRENCIA'
                     , 'LOGRADOURO'
                     , 'LATITUDE'
                     , 'LONGITUDE'
                     , 'CIDADE']

    def Reload(self):
        df = pd.DataFrame()

        for subdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.xlsx'):
                    print(file)
                    base = pd.read_excel(os.path.join(subdir, file))
                    for x in self.cols:
                        try:
                            len(base[x])
                        except:
                            base[x] = np.nan
                    base = base[self.cols]
                    df = pd.concat([df, base], sort=True)
                elif file.endswith('.xls'):
                    try:
                        base = pd.read_table(os.path.join(subdir, file), encoding='utf-8')
                        for x in self.cols:
                            try:
                                len(base[x])
                            except:
                                base[x] = np.nan
                        base = base[self.cols]
                        df = pd.concat([df, base], sort=True)
                    except:
                        print("falha")
                        pass

        df.to_pickle(f"{path_data}\#TransformBO.pkl")
