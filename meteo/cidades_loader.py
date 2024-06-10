

import json

def load_cidades():
    with open('meteo/json/data/cidades.json', 'r') as file:
        return json.load(file)
