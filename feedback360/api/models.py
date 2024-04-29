from django.db import models

# Create your models here.
from django.db import models

class Coordenadores(models.Model):
    idCoordenadores = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

class Cursos(models.Model):
    idCursos = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    codigo = models.CharField(max_length=10)
    Coordenadores_idCoordenadores = models.ForeignKey(Coordenadores, on_delete=models.CASCADE)

class Aluno(models.Model):
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    matricula = models.IntegerField(primary_key=True)
    Cursos_idCursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)

class Disciplina(models.Model):
    idDisciplina = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)

class Competencias(models.Model):
    idCompetencias = models.IntegerField(primary_key=True)
    descricao = models.TextField()
    op1 = models.CharField(max_length=45)
    op2 = models.TextField()
    op3 = models.TextField()
    op4 = models.TextField()
    op5 = models.TextField()

class Professores(models.Model):
    idProfessores = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=100)

class Atividade(models.Model):
    idAtividade = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=45)
    data = models.DateField()

class Turma(models.Model):
    idTurma = models.IntegerField(primary_key=True)
    semestre = models.CharField(max_length=30)
    Professores_idProfessores = models.ForeignKey(Professores, on_delete=models.CASCADE)
    Disciplina_idDisciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

class Nota(models.Model):
    idNota = models.IntegerField(primary_key=True)
    nota = models.CharField(max_length=45)
    data = models.DateField()
    Atividade_idAtividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    Competencias_idCompetencias = models.ForeignKey(Competencias, on_delete=models.CASCADE)
    Professores_idProfessores = models.ForeignKey(Professores, on_delete=models.CASCADE)
    Aluno_matricula = models.ForeignKey(Aluno, on_delete=models.CASCADE)

class Turma_Aluno(models.Model):
    Turma_idTurma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    Disciplina_idDisciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=45)
    Aluno_matricula = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('Turma_idTurma', 'Disciplina_idDisciplina'),)