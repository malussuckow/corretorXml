from django.shortcuts import render
from django.http import HttpResponse


def corretor_View(request):
    return render(request, 'corretor.html')

# Create your views here.
