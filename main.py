from script.simula_request import SimulaRequest
from script.TransformBO import TransformBO


# ajusta_coluna = pd.set_option("display.max_columns", 100)
# ajusta_largura = pd.set_option('display.width', 150)
# ajusta_altura = pd.set_option('display.height', 200)
# ajusta_linhas = pd.set_option('display.max_rows', 100)

# simula a requisicao dos aplicativos de mapas
orig = "Rua Dr. Alfredo Ellis, 50 - Bela Vista, Sao Paulo - SP"
dest = "Avenida Brigadeiro Luis Antonio, 1272 Sao Paulo - SP, Brasil"


# comando de atualizacao dos dados
TransformBO().Reload()
SimulaRequest(_origem=orig, _destino=dest).Reload()

# http://127.0.0.1:8000/v1/score_rota?rotas=teste