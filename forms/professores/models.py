from django.db import models

class Professores(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    disciplinas = models.CharField(max_length=100)

class Disciplinas(models.Model):
    nome = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    turma = models.CharField(max_length=45)
    docente = models.CharField(max_length=45)

class Alunos(models.Model):
    nome = models.CharField(max_length=45)
    matricula = models.IntegerField()
    email = models.EmailField(max_length=100)
    curso = models.CharField(max_length=45)

class Tem(models.Model):
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)

class Competencias(models.Model):
    descricao = models.TextField()
    opcao_1 = models.TextField()
    opcao_2 = models.TextField()
    opcao_3 = models.TextField()
    opcao_4 = models.TextField()
    opcao_5 = models.TextField()
    tem = models.ForeignKey(Tem, on_delete=models.CASCADE)

class Ministra(models.Model):
    professor = models.ForeignKey(Professores, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
