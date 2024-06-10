from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Bandas, Albuns, Musicas
from .forms import BandaForm, AlbumForm, MusicaForm
from django.views.generic.edit import UpdateView
from .forms import AlbunsForm





def bandas_list(request):
    bandas = Bandas.objects.all()
    return render(request, 'bandas/index.html', {'bandas': bandas})

def banda_detail(request, pk):
    try:
        banda = Bandas.objects.get(pk=pk)
    except Bandas.DoesNotExist:
        return HttpResponseNotFound("Banda não encontrada")
    return render(request, 'bandas/banda.html', {'banda': banda})

def album_detail(request, pk):
    try:
        album = Albuns.objects.get(pk=pk)
    except Albuns.DoesNotExist:
        return HttpResponseNotFound("Álbum não encontrado")
    return render(request, 'bandas/album.html', {'album': album})

# Views para criação, edição e exclusão de bandas, álbuns e músicas
def bandas_create(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas_list')
    else:
        form = BandaForm()
    return render(request, 'bandas/form_banda.html', {'form': form})

def bandas_update(request, pk):
    try:
        banda = Bandas.objects.get(pk=pk)
    except Bandas.DoesNotExist:
        return HttpResponseNotFound("Banda não encontrada")

    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', pk=pk)
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/form_banda.html', {'form': form})

def bandas_delete(request, pk):
    try:
        banda = Bandas.objects.get(pk=pk)
    except Bandas.DoesNotExist:
        return HttpResponseNotFound("Banda não encontrada")

    if request.method == 'POST':
        banda.delete()
        return redirect('bandas:bandas_list')
    return render(request, 'bandas/confirm_delete.html', {'object': banda})

def albuns_create(request):
    banda_id = request.GET.get('banda')
    try:
        banda = Bandas.objects.get(pk=banda_id)
    except Bandas.DoesNotExist:
        return HttpResponseNotFound("Banda não encontrada")

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.banda = banda
            album.save()
            return redirect('bandas:banda', pk=banda.id)
    else:
        form = AlbumForm()
    return render(request, 'bandas/form_album.html', {'form': form, 'banda': banda})

def albuns_update(request, pk):
    album = Albuns.objects.get(pk=pk)
    banda = album.banda  # Obtém a banda associada ao álbum
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', pk=banda.pk)  # Redireciona para a página da banda após a edição
    else:
        form = AlbumForm(instance=album)
    return render(request, 'bandas/form_album.html', {'form': form, 'banda': banda})

def albuns_delete(request, pk):
    try:
        album = Albuns.objects.get(pk=pk)
    except Albuns.DoesNotExist:
        return HttpResponseNotFound("Álbum não encontrado")

    if request.method == 'POST':
        album.delete()
        return redirect('bandas:banda', pk=album.banda.id)
    return render(request, 'bandas/confirm_delete.html', {'object': album})

def musicas_create(request):
    album_id = request.GET.get('album')
    try:
        album = Albuns.objects.get(pk=album_id)
    except Albuns.DoesNotExist:
        return HttpResponseNotFound("Álbum não encontrado")

    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            musica = form.save(commit=False)
            musica.album = album
            musica.save()
            return redirect('bandas:album', pk=album.id)
    else:
        form = MusicaForm()
    return render(request, 'bandas/form_musica.html', {'form': form, 'album': album})

def musicas_update(request, pk):
    musica = Musicas.objects.get(pk=pk)
    album = musica.album  # Obtém o álbum associado à música
    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:album', pk=album.pk)  # Redireciona para a página do álbum após a edição
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'bandas/form_musica.html', {'form': form, 'album': album})


def musicas_delete(request, pk):
    try:
        musica = Musicas.objects.get(pk=pk)
    except Musicas.DoesNotExist:
        return HttpResponseNotFound("Música não encontrada")

    if request.method == 'POST':
        musica.delete()
        return redirect('bandas:album', pk=musica.album.id)
    return render(request, 'bandas/confirm_delete.html', {'object': musica})

def capa_fundo_update(request):
    try:
        capa_fundo = CapaFundo.objects.get(pk=1)
    except CapaFundo.DoesNotExist:
        return HttpResponseNotFound("Capa de fundo não encontrada")

    if request.method == 'POST':
        form = CapaFundoForm(request.POST, request.FILES, instance=capa_fundo)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas_list')
    else:
        form = CapaFundoForm(instance=capa_fundo)
    return render(request, 'bandas/form_capa_fundo.html', {'form': form})


class AlbunsUpdateView(UpdateView):
    model = Albuns
    fields = ['titulo', 'ano_lancamento', 'foto', 'capa']  # Adicione outros campos conforme necessário
    template_name = 'bandas/form_album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banda'] = self.object.banda  # Passa a banda para o contexto do template
        return context



def album_create(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, banda=banda)
        if form.is_valid():
            form.save()
            # Redirecionar ou fazer outras operações após a criação do álbum
    else:
        form = AlbunsForm(banda=banda)
    return render(request, 'bandas/form_album.html', {'form': form, 'banda': banda})
