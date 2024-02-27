from django.shortcuts import render
from django.http import HttpResponse
from .form_page import QuestionForm

def home(request):
    form = QuestionForm()
    return render(request, 'professores/home.html', {'form': form})

def saida(request):
    return HttpResponse('Saida')