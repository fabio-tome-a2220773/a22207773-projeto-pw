from django.shortcuts import render

def index_view(request):
    return render(request, "novaapp/lusofona.html")

def index_1(request):
    return render(request, "novaapp/semestre1.html")

def index_2(request):
    return render(request, "novaapp/semestre2.html")
