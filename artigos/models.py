from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    contexto = models.TextField()

    def __str__(self):
        return f"Comentado por {self.artigo.autor.nome} no artigo {self.artigo.titulo}"

class Ratings(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    valor = models.IntegerField()

    def __str__(self):
        return f"Rating {self.valor} para o artigo {self.artigo.titulo}"

