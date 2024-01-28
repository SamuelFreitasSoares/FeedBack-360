from django.db import models

class Q1(models.Model):
    OPCOES = [
        ('A', 'Opção A'),
        ('B', 'Opção B'),
        ('C', 'Opção C'),
        ('D', 'Opção D'),
        ('E', 'Opção E'),
    ]
    opcao = models.CharField(max_length=1, choices=OPCOES)

    def __str__(self):
        return self.opcao




# Create your models here.
