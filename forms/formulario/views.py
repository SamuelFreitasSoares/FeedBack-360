from django.shortcuts import render
from django.http import HttpResponse
from .form_page import Q1Form

# Create your views here.
def home(request):
    form = Q1Form()
    if request.method == 'POST':
        form = Q1Form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form,}
    return render(request, 'formulario/homepage.html', context)

def saida(request):
    return HttpResponse("Saida")