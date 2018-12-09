from script.simula_request import SimulaRequest
from script.TransformBO import TransformBO
import pandas as pd

# ajusta_coluna = pd.set_option("display.max_columns", 100)
# ajusta_largura = pd.set_option('display.width', 150)

# ajusta_altura = pd.set_option('display.height', 200)
# ajusta_linhas = pd.set_option('display.max_rows', 100)

orig = "Rua Dr. Alfredo Ellis, 50 - Bela Vista, Sao Paulo - SP"
dest = "Avenida Brigadeiro Luis Antonio, 1272 Sao Paulo - SP, Brasil"
_df = SimulaRequest(_origem=orig, _destino=dest).Reload()

_df = TransformBO().Reload()

bo = pd.read_pickle("C:\PyShield\data\#TransformBO.pkl")
gmaps = pd.read_pickle("C:\PyShield\data\#request_gmaps.pkl")

def change_in_latitude(miles):
    import math

    earth_radius = 3960.0
    radians_to_degrees = 180.0/math.pi

    return (miles/earth_radius)*radians_to_degrees

def m_to_miles(m):
    return (m/1000) * 0.62137

deslocamento = change_in_latitude(m_to_miles(20))

tot = pd.DataFrame()
for registro in range(len(gmaps)):
    lat_inicial = gmaps.loc[registro, 'start_loc_lat'] - 0.0001 #deslocamento
    lng_inicial = gmaps.loc[registro, 'start_loc_lng'] + 0.0001 #deslocamento
    lat_final = gmaps.loc[registro, 'end_loc_lat'] + 0.0001 #deslocamento
    lng_final = gmaps.loc[registro, 'end_loc_lng'] - 0.0001 #deslocamento

    calc = bo[(bo.LATITUDE.between(gmaps.loc[registro, 'start_loc_lat'] - deslocamento, gmaps.loc[registro, 'end_loc_lat'] + deslocamento)) & (bo.LONGITUDE.between(gmaps.loc[registro, 'start_loc_lng'] - deslocamento, gmaps.loc[registro, 'end_loc_lng'] + deslocamento))]
    calc['ind'] = registro

    tot = pd.concat([calc, tot])

tot['ANO-MES'] = tot['DATAOCORRENCIA'].apply(str).str[:7]
tot['LOGRADOURO'] = tot['LOGRADOURO'].apply(str)

tot = tot.groupby(['ANO-MES', 'CIDADE', 'LOGRADOURO']).DATAOCORRENCIA.count().reset_index()
