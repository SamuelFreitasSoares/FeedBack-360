from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    option5 = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Form(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Formulário do Professor {self.professor.username}"
