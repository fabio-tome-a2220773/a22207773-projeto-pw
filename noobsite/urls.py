from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view),
    path('indexx/',views.index_mid),
    path('indexxx/',views.index_noob),
    path('indexxxx/',views.index_final),
]