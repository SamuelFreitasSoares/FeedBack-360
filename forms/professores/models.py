from django.db import models
from formulario import models as form
# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=550)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    option5 = models.CharField(max_length=500)

    def __str__(self):
        return self.text

class Form(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Formulário do Professor {self.professor.username}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    curso = models.CharField(max_length=100)