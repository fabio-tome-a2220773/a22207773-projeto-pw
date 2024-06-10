from django import forms
from .models import Autor, Artigo, Comentario, Ratings

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'texto', 'autor']
