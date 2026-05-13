from django.shortcuts import render
from xml_upload.forms_professor import Upload_xml_professor
from .forms import Upload_xmlForm
from corretor.models import Exercicio, Submissao
from usuarios.models import Aluno, Professor
from django.shortcuts import render, redirect
from django.contrib import messages
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def upload_xml(request):
    form = Upload_xmlForm(request.POST or None, request.FILES or None)
    if  request.method == 'POST' and form.is_valid():
        arquivo = form.cleaned_data['arquivo_xml']
        arquivo_Professor = form.cleaned_data['arquivo_xml_professor'] 
        messages.success(request, 'Arquivos XML enviados com sucesso!')

        return redirect('upload')
        
    return render(request, 'upload_aluno.html', {'form': form})

@login_required(login_url='login')
def upload_xml_professor(request):
    form = Upload_xml_professor(request.POST or None, request.FILES or None)
    if  request.method == 'POST' and form.is_valid():
        arquivo = form.cleaned_data['xml_base']
        Exercicio.objects.create(
            titulo=form.cleaned_data['titulo'], 
            descricao=form.cleaned_data['descricao'],
            professor=request.user.professor,
            xml_base=arquivo.read().decode('utf-8')
        )
        messages.success(request, 'Arquivo XML enviado com sucesso!')

        return redirect('upload_professor')

    return render(request, 'upload_professor.html', {'form': form})

