from django.urls import path
from . import views

app_name = 'pwsite'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('sobre/', views.index_sobre, name='index_sobre'),
    path('interesses/', views.index_interesses, name='index_interesses'),
]

