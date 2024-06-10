from django.urls import path
from . import views

app_name = 'LIG'

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos_list, name='cursos_list'),
    path('curso/<int:curso_id>/', views.curso_detail, name='curso_detail'),
    path('disciplinas/', views.disciplinas_list, name='disciplinas_list'),
    path('disciplina/<int:disciplina_id>/', views.disciplina_detail, name='disciplina_detail'),
    path('projeto/<int:projeto_id>/', views.projeto_detail, name='projeto_detail'),
    path('cursos/novo', views.novo_curso_view,name="novo_curso"),
    path('cursos/<int:curso_id>/edita', views.edita_curso_view,name="edita_curso"),
    path('cursos/<int:curso_id>/apaga', views.apaga_curso_view,name="apaga_curso"),
]
