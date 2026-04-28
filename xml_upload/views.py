from django.shortcuts import render
from .forms import Upload_xmlForm
from django.shortcuts import render, redirect
from django.contrib import messages
import xml.etree.ElementTree as ET

def upload_xml(request):
    form = Upload_xmlForm(request.POST or None, request.FILES or None)
    if  request.method == 'POST' and form.is_valid():
        arquivo = form.cleaned_data['arquivo_xml']
        arquivo_Professor = form.cleaned_data['arquivo_xml_professor'] 
        messages.success(request, 'Arquivos XML enviados com sucesso!')

        return redirect('upload')
        
    return render(request, 'upload.html', {'form': form})



# Create your views here.
