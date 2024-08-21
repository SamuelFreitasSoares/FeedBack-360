from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    matricula = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Coordenador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField('Curso')

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=50, unique=True)
    coordenadores = models.ManyToManyField(Coordenador)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    descricao = models.CharField(max_length=255)
    opcao = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    notas = models.ManyToManyField('Nota', related_name='competencias')


class Atividade(models.Model):
    titulo = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Aluno, related_name='avaliador', on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    data = models.DateField()

    def __str__(self):
        return f'{self.aluno} - {self.atividade} - {self.nota}'

class Turma(models.Model):
    semestre = models.CharField(max_length=50)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.disciplina} - {self.semestre}'

class TurmaAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=50)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('aluno', 'turma', 'disciplina')

    def __str__(self):
        return f'{self.aluno} - {self.turma} - {self.disciplina}'
