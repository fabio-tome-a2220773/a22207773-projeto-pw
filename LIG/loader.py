import json
from .models import Curso, Disciplina, Area_Cientifica, Linguagem_Programacao, Projeto, Docente

SEMESTRE_MAP = {
    "1º Semestre": 1,
    "2º Semestre": 2,
    "3º Semestre": 3,
    "4º Semestre": 4,
    "5º Semestre": 5,
    "6º Semestre": 6,
    "Anual": 0,
}

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)


        curso_dados = dados['courseDetail']
        curso, criado = Curso.objects.get_or_create(
            nome=curso_dados['courseName'],
            apresentacao=curso_dados['presentation'],
            objetivos=curso_dados['objectives'],
            competencias=curso_dados['competences'],

        )


        disciplinas_dados = dados['courseFlatPlan']
        for disciplina_dados in disciplinas_dados:
            semestre_str = disciplina_dados['semester']
            semestre = SEMESTRE_MAP.get(semestre_str)
            if semestre is None:
                raise ValueError(f"Semestre inválido: {semestre_str}")


            area_cientifica_nome = disciplina_dados.get('scientificArea', 'Área Científica Padrão')
            area_cientifica, _ = Area_Cientifica.objects.get_or_create(nome=area_cientifica_nome)


            disciplina, criada = Disciplina.objects.get_or_create(
                nome=disciplina_dados['curricularUnitName'],
                ano=disciplina_dados['curricularYear'],
                semestre=semestre,
                ects=disciplina_dados['ects'],
                curricular_unit_readable_code=disciplina_dados['curricularIUnitReadableCode'],
                area_cientifica=area_cientifica,
                curso=curso,

            )


            projeto_dados = disciplina_dados.get('project')
            if projeto_dados:
                projeto, _ = Projeto.objects.get_or_create(
                    disciplina=disciplina,
                    descricao=projeto_dados['description'],
                    conceitos_aplicados=projeto_dados['appliedConcepts'],
                    tecnologias_utilizadas=projeto_dados['technologies'],
                    imagem=projeto_dados['image'],
                    video_youtube=projeto_dados['youtubeVideo'],
                    repositorio_github=projeto_dados.get('githubRepository'),

                )


    print("Dados carregados com sucesso!")

# Caminho para o arquivo JSON
caminho_arquivo_json = 'LIG/json/informação.json'

# Chamada da função para carregar os dados
carregar_dados_json(caminho_arquivo_json)
