import json
from bandas.models import Bandas, Albuns, Musicas

Bandas.objects.all().delete()
Albuns.objects.all().delete()
Musicas.objects.all().delete()


with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    for info in bandas:
        print(info['nome'], info['nacionalidade'], info['ano_criacao'])

        banda = Bandas.objects.create(
            nome=info['nome'],
            nacionalidade=info['nacionalidade'],
            ano_criacao=info['ano_criacao']
        )

        print(banda)

with open('bandas/json/discos.json') as f:
    discos = json.load(f)

    for disco in discos:
        titulo = disco['titulo']
        ano_lancamento = disco['ano_lancamento']
        banda_nome = disco['banda']

        banda = Bandas.objects.get(nome=banda_nome)

        album = Albuns.objects.create(
            titulo=titulo,
            ano_lancamento=ano_lancamento,
            banda=banda
        )

        print(album)

        for musica in disco['musicas']:
            titulo_musica = musica['titulo']
            duracao = musica['duracao']

            musica_obj = Musicas.objects.create(
                titulo=titulo_musica,
                album=album,
                duracao=duracao
            )

            print(musica_obj)
