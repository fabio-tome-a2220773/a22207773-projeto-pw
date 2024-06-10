from django.shortcuts import render


def index_view(request):
    return render(request, "pwsite/index.html")

def index_sobre(request):
    return render(request, "pwsite/sobre.html")

def index_interesses(request):
    return render(request, "pwsite/interesses.html")



