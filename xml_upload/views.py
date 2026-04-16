from django.shortcuts import render
from django.http import HttpResponse

def upload_View(request):
    return render(request, 'upload.html')


# Create your views here.
