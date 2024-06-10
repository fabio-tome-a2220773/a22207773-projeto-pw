from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.layout_view, name='layout'),
    path('autores/', views.autores_view, name='autores'),
    path('autores/<int:autor_id>/', views.autor_detalhes_view, name='autor_detalhes'),  # Nova rota
    path('artigos/', views.artigos_view, name='artigos'),
    path('adicionar_autor/', views.adicionar_autor, name='adicionar_autor'),
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),
    path('excluir_autor/<int:autor_id>/', views.excluir_autor, name='excluir_autor'),
    path('adicionar_artigo/', views.adicionar_artigo, name='adicionar_artigo'),
    path('editar_artigo/<int:artigo_id>/', views.editar_artigo, name='editar_artigo'),
    path('excluir_artigo/<int:artigo_id>/', views.excluir_artigo, name='excluir_artigo'),
]
