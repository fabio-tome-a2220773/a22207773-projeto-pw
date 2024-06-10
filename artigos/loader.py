import json
from artigos.models import Autor, Artigo


with open('artigos/json/autores.json') as f:
    autores = json.load(f)

    for autor_data in autores:
        nome = autor_data['nome']
        autor, created = Autor.objects.get_or_create(nome=nome)
        if created:
            print("Autor criado:", autor)


with open('artigos/json/artigos.json') as f:
    artigos = json.load(f)

    for artigo_data in artigos:
        titulo = artigo_data['titulo']
        texto = artigo_data['texto']
        autor_nome = artigo_data['autor']

        autor = Autor.objects.get(nome=autor_nome)

        artigo, created = Artigo.objects.get_or_create(
            titulo=titulo,
            texto=texto,
            autor=autor
        )

        if created:
            print("Artigo criado:", artigo)
