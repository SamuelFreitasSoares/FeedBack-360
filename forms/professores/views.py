from django.shortcuts import render
from django.http import HttpResponse
from formulario.models import Q1, Q2, Aluno
import csv
from .form_page import QuestionForm, UploadFileForm

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csvfile = request.FILES['file']
            reader = csv.DictReader(csvfile)
            for row in reader:
                Aluno.objects.create(
                    nome=row['Nome'],
                    matricula=row['Matrícula'],
                    curso=row['Curso']
                    # Adicione outros campos conforme necessário
                )
            return render(request, 'professores/upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'professores/upload.html', {'form': form})

