from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('lusofona/', views.index_view, name='lusofona'),
    path('semestre1/', views.index_1, name='semestre1'),
    path('semestre2/', views.index_2, name='semestre2'),
]