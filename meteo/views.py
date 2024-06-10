import requests
from django.shortcuts import render
from .models import City
from datetime import datetime









def meteo_home(request):
    return render(request, 'meteo/home.html')

def get_weather_data():
    # Endpoint para a previsão do tempo em Lisboa
    forecast_url = 'http://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    # Endpoint para as classes de tempo
    weather_classes_url = 'http://api.ipma.pt/open-data/weather-type-classe.json'

    forecast_response = requests.get(forecast_url)
    classes_response = requests.get(weather_classes_url)

    if forecast_response.status_code == 200 and classes_response.status_code == 200:
        forecast_data = forecast_response.json()
        classes_data = classes_response.json()
        return forecast_data, classes_data
    else:
        return None, None

def process_weather_data(forecast_data, classes_data):
    # Pegando a previsão para hoje
    today_forecast = forecast_data['data'][0]
    min_temp = today_forecast['tMin']
    max_temp = today_forecast['tMax']
    date = today_forecast['forecastDate']
    id_weather_type = today_forecast['idWeatherType']

    # Depuração para verificar os dados retornados
    print("Classes Data:", classes_data)

    # Encontrando a descrição do tempo
    weather_description = next(
        (item.get('descIdWeatherTypePT', item.get('descWeatherTypePT', 'Descrição não encontrada')) for item in classes_data['data'] if item['idWeatherType'] == id_weather_type),
        "Descrição não encontrada"
    )

    # Construindo o caminho para o ícone animado local
    icon_url = f"/static/meteo/icons/icons_ipma_weather/w_ic_d_{id_weather_type:02d}anim.svg"  # Caminho local baseado no idWeatherType

    return {
        'city': 'Lisboa',
        'min_temp': min_temp,
        'max_temp': max_temp,
        'date': date,
        'description': weather_description,
        'icon_url': icon_url
    }



def lisbon_weather(request):
    forecast_data, classes_data = get_weather_data()
    if forecast_data and classes_data:
        weather_info = process_weather_data(forecast_data, classes_data)
    else:
        weather_info = None
    return render(request, 'meteo/lisbon_weather.html', {'weather_info': weather_info})



def get_cities():
    cities_url = 'http://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        data = response.json()
        return data['data']
    return []

def get_weather_forecast(city_id):
    forecast_url = f"https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json"
    response = requests.get(forecast_url)
    if response.status_code == 200:
        data = response.json()
        # Obtenha a URL das classes de tempo para mapear idWeatherType para descrições e ícones
        weather_classes_url = 'http://api.ipma.pt/open-data/weather-type-classe.json'
        classes_response = requests.get(weather_classes_url)
        if classes_response.status_code == 200:
            classes_data = classes_response.json()
            for day_forecast in data['data']:
                id_weather_type = day_forecast['idWeatherType']
                weather_description = next(
                    (item.get('descIdWeatherTypePT', item.get('descWeatherTypePT', 'Descrição não encontrada')) for item in classes_data['data'] if item['idWeatherType'] == id_weather_type),
                    "Descrição não encontrada"
                )
                icon_url = f"/static/meteo/icons/icons_ipma_weather/w_ic_d_{id_weather_type:02d}anim.svg"
                day_forecast['weatherDescription'] = weather_description
                day_forecast['icon_url'] = icon_url
            return data['data']  # Retorna apenas a lista de previsões
    return None

def weather_forecast(request):
    cities = get_cities()
    selected_city = None
    forecast_data = None
    selected_date = None
    forecast_for_selected_date = None

    if request.method == 'POST':
        selected_city_id = request.POST.get('city')
        selected_date = request.POST.get('date')
        if selected_city_id:
            selected_city = next(city for city in cities if city['globalIdLocal'] == int(selected_city_id))
            forecast_data = get_weather_forecast(selected_city_id)
            if selected_date and forecast_data:
                selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
                forecast_for_selected_date = next((forecast for forecast in forecast_data if datetime.strptime(forecast['forecastDate'], '%Y-%m-%d').date() == selected_date), None)

    return render(request, 'meteo/weather_forecast.html', {
        'cities': cities,
        'selected_city': selected_city,
        'forecast_data': forecast_data,
        'selected_date': selected_date,
        'forecast_for_selected_date': forecast_for_selected_date
    })





