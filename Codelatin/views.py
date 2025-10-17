from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def inicio(request):
    return render(request, 'inicio.html')