from django.shortcuts import render
from django.http import HttpResponse
from .form_page import *

# Create your views here.
def home(request):
    q1_form = Q1Form(prefix='q1')
    q2_form = Q2Form(prefix='q2')  
    if request.method == 'POST':
        q1_form = Q1Form(request.POST, prefix='q1')
        q2_form = Q2Form(request.POST, prefix='q2') 
        if q1_form.is_valid():
            q1_form.save()
        if q2_form.is_valid():  
            q2_form.save()
    context = {
        'q1_form': q1_form,
        'q2_form': q2_form, 
    }
    return render(request, 'formulario/homepage.html', context)

def saida(request):
    return HttpResponse("Saida")