from django.shortcuts import render
from .models import Localizacao, Festival

def lista_festivais(request):
    localizacoes = Localizacao.objects.all()
    return render(request, 'festivais/lista_festivais.html', {'localizacoes': localizacoes})

def detalhes_festival(request, festival_id):
    festival = Festival.objects.get(pk=festival_id)
    return render(request, 'festivais/detalhes_festival.html', {'festival': festival})



