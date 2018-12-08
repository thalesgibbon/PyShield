key = 'AIzaSyBX3xepu_rRch5QfB_bc-mB4hHj3b-ecUQ'
origem = "Disneyland"
destino = "Universal Studios Hollywood"

origem = origem.replace(' ', '+')
destino = destino.replace(' ', '+')

url = "https://maps.googleapis.com/maps/api/directions/json?origin={origem}&destination={destino}&key={chave}"
