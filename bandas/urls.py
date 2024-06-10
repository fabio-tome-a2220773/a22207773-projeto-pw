from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.bandas_list, name='bandas_list'),
    path('banda/<int:pk>/', views.banda_detail, name='banda'),
    path('album/<int:pk>/', views.album_detail, name='album'),
    path('banda/novo/', views.bandas_create, name='banda_create'),
    path('banda/editar/<int:pk>/', views.bandas_update, name='banda_update'),
    path('banda/excluir/<int:pk>/', views.bandas_delete, name='banda_delete'),
    path('album/novo/', views.albuns_create, name='album_create'),
    path('album/editar/<int:pk>/', views.albuns_update, name='album_update'),
    path('album/excluir/<int:pk>/', views.albuns_delete, name='album_delete'),
    path('musica/novo/', views.musicas_create, name='musica_create'),
    path('musica/editar/<int:pk>/', views.musicas_update, name='musica_update'),
    path('musica/excluir/<int:pk>/', views.musicas_delete, name='musica_delete'),
    path('capa-fundo/', views.capa_fundo_update, name='capa_fundo_update'),
]
