from django.shortcuts import render
import requests


def Icon():
    previsao_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json"
    previsao_response = requests.get(previsao_url)
    previsao_data = previsao_response.json()
    hoje_previsao = previsao_data['data'][0]

    id_weather_type = hoje_previsao['idWeatherType']
    icon_url = f"/static/meteo/icons/icons_ipma_weather/w_ic_d_{id_weather_type:02d}anim.svg"

    return icon_url

def landing_page(request):
    icon_url = Icon()
    context = {
        'icon_url': icon_url,
    }
    return render(request, 'portfolio/landing_page.html', context)

def mebyme(request):
    return render(request, 'portfolio/mebyme.html')

def sobre(request):
    return render(request, 'portfolio/mebyme_tech.html')