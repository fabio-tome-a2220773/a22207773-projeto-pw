
import json

def load_previsao_hoje():
    with open('meteo/json/data/previsao_hoje.json', 'r') as file:
        return json.load(file)
