from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=3)
    periodo = models.IntegerField()

    def __str__(self):
        return self.nome

class Q1(models.Model):
    OPCOES = [
        ('1', 'Nenhum dos  requisitos/necessidades foram identificados e validados com os usuários'),
        ('2', 'Alguns dos requisitos/necessidades foram identificados e validados com os usuários (30 %)'),
        ('3', 'A maior parte dos requisitos/necessidades foram identificados e validados com os usuários (70 %)'),
        ('4', 'Todos os requisitos/necessidades foram identificados e validados com os usuários'),
        ('5', 'Foram levantados  e validados requisitos/necessidades além dos inicialmente solicitados, agregando valor ao projeto.'),
    ]
    opcao = models.CharField(max_length=1, choices=OPCOES)

    def __str__(self):
        return self.opcao

class Q2(models.Model):
    OPCOES = [
        ('1', 'A solução apresentada não atendeu as expectativas  '),
        ('2', 'A solução apresentada atendeu minimamente as expectativas'),
        ('3', 'A solução apresentada atendeu parcialmente as expectativas  '),
        ('4', 'A solução apresentada atendeu plenamente as expectativas  '),
        ('5', 'A solução apresentada excedeu as expectativas  '),
    ]
    opcao = models.CharField(max_length=1, choices=OPCOES)

    def __str__(self):
        return self.opcao



# Create your models here.
