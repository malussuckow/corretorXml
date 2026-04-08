from django.shortcuts import render
from django.http import HttpResponse

def home_View(request):
    return HttpResponse("Bem-vindo à página inicial do Corretor XML!")

# Create your views here.
