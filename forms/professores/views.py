from django.shortcuts import render
from django.http import HttpResponse
from formulario.models import Q1, Q2

# Create your views here.
def init(request):
    return render(request, 'professores/home.html')

def saida(request):
    return HttpResponse('Saida')

