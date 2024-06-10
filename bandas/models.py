from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Bandas(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    ano_criacao = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    foto = models.ImageField(upload_to='banda_fotos/')
    bio = models.TextField()

    def __str__(self):
        return self.nome


class Albuns(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])
    foto = models.ImageField(upload_to='banda_fotos/', blank=True)
    capa = models.ImageField(upload_to='capa_fotos/', blank=True)
    banda = models.ForeignKey(Bandas, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Musicas(models.Model):
    titulo = models.CharField(max_length=100)
    duracao = models.TimeField()
    link = models.URLField(blank=True, validators=[URLValidator()])
    album = models.ForeignKey(Albuns, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Capafundo(models.Model):
    nome = models.CharField(max_length=100,blank=True)
    foto = models.ImageField(upload_to='capas_fundo/',blank=True)

    def __str__(self):
        return self.nome
