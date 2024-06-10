from django import forms
from .models import Bandas, Albuns, Musicas

class BandaForm(forms.ModelForm):
    class Meta:
        model = Bandas
        fields = ['nome', 'nacionalidade', 'ano_criacao', 'foto', 'bio']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albuns
        fields = ['titulo', 'ano_lancamento', 'foto', 'capa', 'banda']

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musicas
        fields = ['titulo', 'duracao', 'link', 'album']




class AlbunsForm(forms.ModelForm):
    class Meta:
        model = Albuns
        fields = ['titulo', 'ano_lancamento', 'foto', 'capa']  # Adicione outros campos conforme necessário

    def __init__(self, banda, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.banda = banda

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.banda = self.banda
        if commit:
            instance.save()
        return instance