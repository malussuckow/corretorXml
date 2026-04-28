from django.shortcuts import render

def Cadastro_View(request):
    return render(request, 'usuarios/cadastro.html')

def Login_View(request):
    return render(request, 'usuarios/login.html')
# Create your views here.
