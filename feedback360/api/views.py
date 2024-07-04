import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Coordenadores, Cursos, Aluno, Disciplina, Competencias, Professores, Atividade, Turma, Nota, Turma_Aluno
from .forms import CSVUploadForm
from io import TextIOWrapper

def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            data = TextIOWrapper(file.file, encoding='utf-8')
            reader = csv.DictReader(data)
            
            for row in reader:

                # Coordenadores
                coordenador, created = Coordenadores.objects.get_or_create(
                    idCoordenadores=row['idCoordenadores'],
                    defaults={'nome': row['nome_coordenador'], 'email': row['email_coordenador']}
                )

                # Cursos
                curso, created = Cursos.objects.get_or_create(
                    idCursos=row['idCursos'],
                    defaults={'nome': row['nome_curso'], 'codigo': row['codigo_curso'], 'Coordenadores_idCoordenadores': coordenador}
                )

                # Aluno
                aluno, created = Aluno.objects.get_or_create(
                    matricula=row['matricula_aluno'],
                    defaults={'nome': row['nome_aluno'], 'email': row['email_aluno'], 'Cursos_idCursos': curso}
                )

                # Disciplina
                disciplina, created = Disciplina.objects.get_or_create(
                    idDisciplina=row['idDisciplina'],
                    defaults={'nome': row['nome_disciplina'], 'codigo': row['codigo_disciplina']}
                )

                # Competencias
                competencia, created = Competencias.objects.get_or_create(
                    idCompetencias=row['idCompetencias'],
                    defaults={'descricao': row['descricao_competencia'], 'op1': row['op1'], 'op2': row['op2'], 'op3': row['op3'], 'op4': row['op4'], 'op5': row['op5']}
                )

                # Professores
                professor, created = Professores.objects.get_or_create(
                    idProfessores=row['idProfessores'],
                    defaults={'nome': row['nome_professor'], 'email': row['email_professor']}
                )

                # Atividade
                atividade, created = Atividade.objects.get_or_create(
                    idAtividade=row['idAtividade'],
                    defaults={'titulo': row['titulo_atividade'], 'data': row['data_atividade']}
                )

                # Turma
                turma, created = Turma.objects.get_or_create(
                    idTurma=row['idTurma'],
                    defaults={'semestre': row['semestre_turma'], 'Professores_idProfessores': professor, 'Disciplina_idDisciplina': disciplina}
                )

                # Nota
                nota, created = Nota.objects.get_or_create(
                    idNota=row['idNota'],
                    defaults={
                        'nota': row['nota'],
                        'data': row['data_nota'],
                        'Atividade_idAtividade': atividade,
                        'Competencias_idCompetencias': competencia,
                        'Professores_idProfessores': professor,
                        'Aluno_matricula': aluno
                    }
                )

                # Turma_Aluno
                turma_aluno, created = Turma_Aluno.objects.get_or_create(
                    Turma_idTurma=turma,
                    Disciplina_idDisciplina=disciplina,
                    semestre=row['semestre'],
                    Aluno_matricula=aluno
                )

            return HttpResponseRedirect('/success/url/')
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})
