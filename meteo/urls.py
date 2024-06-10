from django.urls import path
from .views import lisbon_weather, meteo_home, weather_forecast



app_name = 'meteo'

urlpatterns = [
    path('', meteo_home, name='home'),
    path('lisbon/', lisbon_weather, name='lisbon_weather'),
    path('forecast/', weather_forecast, name='weather_forecast'),


]
