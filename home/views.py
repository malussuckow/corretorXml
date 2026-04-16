from django.shortcuts import render
from django.http import HttpResponse

def home_View(request):
    return render(request, 'home.html')

# Create your views here.
