from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>TestNet</h4>")

def about(request):
    return HttpResponse("<h1>TestAbout</h4>")

def html(request):
    name = input()  # Пример динамических данных
    return render(request, 'index.html', {'name': name})