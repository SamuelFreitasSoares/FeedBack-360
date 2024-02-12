from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'professores/home.html')

def saida(request):
    return HttpResponse('Saida')