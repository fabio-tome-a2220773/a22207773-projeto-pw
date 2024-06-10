from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome


class Area_Cientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.DecimalField(max_digits=5, decimal_places=2)
    curricular_unit_readable_code = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(Area_Cientifica, on_delete=models.CASCADE)
    docentes = models.ManyToManyField('Docente',blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')
    projeto = models.OneToOneField('Projeto', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome



class Linguagem_Programacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Projeto(models.Model):
    nome = models.CharField(max_length=100,blank=True)
    descricao = models.TextField(blank=True, null=True)
    conceitos_aplicados = models.TextField(blank=True, null=True)
    tecnologias_utilizadas = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='projeto_images/', blank=True, null=True)
    video_youtube = models.URLField(blank=True, null=True)
    repositorio_github = models.URLField(blank=True, null=True)
    linguagens_programacao = models.ManyToManyField(Linguagem_Programacao, blank=True)

    def __str__(self):
        return self.nome



class Docente(models.Model):
    nome = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.nome
