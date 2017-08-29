from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Rango index says hey!")

def about(request):
    return HttpResponse("rango about say hi")

