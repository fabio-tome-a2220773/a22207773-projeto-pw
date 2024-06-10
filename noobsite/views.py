from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def index_mid(request):
    return HttpResponse("Vais aprender a fazer sites bonitos")

def index_noob(request):
    return HttpResponse("Não sejas noob")

def index_final(request):
    return HttpResponse("Boa sorte!")


