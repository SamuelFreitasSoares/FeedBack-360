from django import forms
from . import models


class Questoes(forms.ModelForm):
    text = models.CharField(max_length=255)
    
    
    resp = forms.ChoiceField()