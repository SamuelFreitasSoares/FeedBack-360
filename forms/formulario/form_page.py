from django import forms
from .models import *

class Q1Form(forms.ModelForm):
    RESPOSTAS = (
        ('1', 'Nenhum dos  requisitos/necessidades foram identificados e validados com os usuários'),
        ('2', 'Alguns dos requisitos/necessidades foram identificados e validados com os usuários (30 %)'),
        ('3', 'A maior parte dos requisitos/necessidades foram identificados e validados com os usuários (70 %)'),
        ('4', 'Todos os requisitos/necessidades foram identificados e validados com os usuários'),
        ('5', 'Foram levantados  e validados requisitos/necessidades além dos inicialmente solicitados, agregando valor ao projeto.'),
    )

    opcao = forms.ChoiceField(label="Os requisitos/necessidades foram identificados e validados com os usuários? ", choices=RESPOSTAS, widget=forms.RadioSelect, required=False)
    
    class Meta:
        model = Q1
        fields = ['opcao']
        labels = {'opcao': 'Opção'}

class Q2Form(forms.ModelForm):
    RESPOSTAS = (
        ('1', 'A solução apresentada não atendeu as expectativas  '),
        ('2', 'A solução apresentada atendeu minimamente as expectativas'),
        ('3', 'A solução apresentada atendeu parcialmente as expectativas  '),
        ('4', 'A solução apresentada atendeu plenamente as expectativas  '),
        ('5', 'A solução apresentada excedeu as expectativas  '),
    )

    opcao = forms.ChoiceField(label="A solução apresentada atendeu aos requisitos/necessidades? ", choices=RESPOSTAS, widget=forms.RadioSelect, required=False)
    
    class Meta:
        model = Q2
        fields = ['opcao']
        labels = {'opcao': 'Opção'}
