import requests
from time import sleep
import pandas as pd
from __config__ import purge_full, path_data


class SimulaRequest(object):
    def __init__(self, _origem, _destino):
        self.chave = 'AIzaSyAhBPTr4-yu20co7eAkJUosvsiE6VLZS-I'
        self.mode = 'walking'

        self.origem = _origem.translate(purge_full).replace(' ', '+').replace('++', '+')
        self.destino = _destino.translate(purge_full).replace(' ', '+').replace('++', '+')

        self.url = f"https://maps.googleapis.com/maps/api/directions/json?origin={self.origem}&destination={self.destino}&mode={self.mode}&key={self.chave}"

    def Reload(self):
        # falha na rede, fazer 10 tentativas
        for n in range(10):
            r = requests.get(url=self.url)
            r_json = r.json()
            r_dict = dict(r_json)
            try:
                if r_dict ['geocoded_waypoints'][0]['geocoder_status'] == 'OK':
                    break
            except:
                sleep(1)

        # dicionario com rota sugerida
        r_dict = r_dict['routes'][0]['legs'][0]['steps']

        # transformanado para dataframe
        dicio_ruas = {}
        for id, rua in enumerate(r_dict):
            cols = ['distancia', 'start_loc_lat', 'start_loc_lng', 'end_loc_lat', 'end_loc_lng']
            distancia = rua['distance']['value']
            start_loc_lat = rua['start_location']['lat']
            start_loc_lng = rua['start_location']['lng']
            end_loc_lat = rua['end_location']['lat']
            end_loc_lng = rua['end_location']['lng']

            dicio_ruas[id] = [distancia, start_loc_lat, start_loc_lng, end_loc_lat, end_loc_lng]

        df = pd.DataFrame.from_dict(dicio_ruas, orient='index', columns=cols)

        df.to_pickle(f"{path_data}\#request_gmaps.pkl")
