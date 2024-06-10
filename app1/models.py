from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    idade = models.IntegerField()


    def __str__(self):
        return f'{self.name} - {self.idade} anos'

class Aluno(models.Model):
    name = models.CharField(max_length=100)



# Create your models here.
