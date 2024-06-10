from django.urls import path
from . import views

urlpatterns = [
    path('festivais/', views.lista_festivais, name='lista_festivais'),
    path('festival/<int:festival_id>/', views.detalhes_festival, name='detalhes_festival'),
]
