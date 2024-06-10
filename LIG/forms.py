from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder':'Nome completo',
            })
        }
