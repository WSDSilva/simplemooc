from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html', {'usuario':'Wanderson'})

def contact(request):
    return render(request, 'contato.html')
