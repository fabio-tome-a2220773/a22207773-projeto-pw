from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Docente, Projeto
from .forms import CursoForm


def index(request):
    return render(request, 'LIG/index.html')

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'LIG/cursos_list.html', {'cursos': cursos})

def curso_detail(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    disciplinas = curso.disciplinas.all()
    return render(request, 'LIG/curso_detail.html', {'curso': curso, 'disciplinas': disciplinas})

def disciplinas_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'LIG/disciplinas_list.html', {'disciplinas': disciplinas})

def disciplina_detail(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    docentes = disciplina.docentes.all()
    projeto = disciplina.projeto
    return render(request, 'LIG/disciplina_detail.html', {'disciplina': disciplina, 'docentes': docentes, 'projeto': projeto})

def projeto_detail(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    return render(request, 'LIG/projeto_detail.html', {'projeto': projeto})


@login_required
def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('LIG:cursos_list')
    context = {'form': form}
    return render(request, 'LIG/novo_curso.html', context)

@login_required
def edita_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('LIG:cursos_list')
    context = {'form': form, 'curso': curso}
    return render(request, 'LIG/edita_curso.html', context)

@login_required
def apaga_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    return redirect('LIG:cursos_list')

@login_required
def novo_projeto_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.disciplina = disciplina
            projeto.save()
            return redirect('LIG:disciplina_detail', disciplina_id=disciplina_id)
    else:
        form = ProjetoForm()
    return render(request, 'LIG/novo_projeto.html', {'form': form, 'disciplina': disciplina})



