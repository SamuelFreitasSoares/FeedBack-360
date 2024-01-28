from django import forms
from .models import Q1

class Q1Form(forms.ModelForm):
    RESPOSTAS = (
        ('A', 'Opção A'),
        ('B', 'Opção B'),
        ('C', 'Opção C'),
        ('D', 'Opção D'),
        ('E', 'Opção E'),
    )

    opcao = forms.ChoiceField(choices=RESPOSTAS, widget=forms.RadioSelect, required=False)

    class Meta:
        model = Q1
        fields = ['opcao']
        labels = {'opcao': 'Opção'}
