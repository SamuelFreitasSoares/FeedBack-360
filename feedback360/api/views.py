import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import *
import io

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']

        # Verifica se o arquivo é um CSV
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'O arquivo deve ser um CSV.')
            return redirect('upload_csv')

        # Lê o conteúdo do arquivo CSV
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Pula o cabeçalho

        # Processa cada linha do CSV
        for row in csv.reader(io_string, delimiter=','):
            nome, email = row
            # Verifica se o aluno já existe
            if not Aluno.objects.filter(email=email).exists():
                Aluno.objects.create(nome=nome, email=email)
            else:
                messages.warning(request, f'O aluno com o email {email} já está cadastrado.')

        messages.success(request, 'Alunos cadastrados com sucesso.')
        return redirect('upload_csv')

    return render(request, 'upload_csv.html')
    
