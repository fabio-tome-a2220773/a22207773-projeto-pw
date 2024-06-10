from django.shortcuts import render, redirect, get_object_or_404
from .models import Artigo, Autor
from .forms import AutorForm, ArtigoForm

def layout_view(request):
    context = {}
    return render(request, 'artigos/layout.html', context)

def autores_view(request):
    autores = Autor.objects.all()
    context = {'autores': autores}
    return render(request, 'artigos/autores.html', context)

def artigos_view(request):
    artigos = Artigo.objects.all()
    context = {'artigos': artigos}
    return render(request, 'artigos/artigos.html', context)

def autor_detalhes_view(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    artigos = Artigo.objects.filter(autor=autor)
    context = {
        'autor': autor,
        'artigos': artigos
    }
    return render(request, 'artigos/autor_detalhes.html', context)

def adicionar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:autores')
    else:
        form = AutorForm()
    return render(request, 'artigos/adicionar_autor.html', {'form': form})

def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('artigos:autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'artigos/editar_autor.html', {'form': form})

def excluir_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('artigos:autores')
    return render(request, 'artigos/excluir_autor.html', {'autor': autor})

def adicionar_artigo(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/adicionar_artigo.html', {'form': form})

def editar_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:artigos')
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/editar_artigo.html', {'form': form})

def excluir_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:artigos')
    return render(request, 'artigos/excluir_artigo.html', {'artigo': artigo})
