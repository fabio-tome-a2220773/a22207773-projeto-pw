
import json

def load_previsao_5_dias():
    with open('meteo/json/data/previsao_5_dias.json', 'r') as file:
        return json.load(file)
