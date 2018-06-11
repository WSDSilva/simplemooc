from django.shortcuts import render
from .models import Course 

def index(request):
    cursos = Course.objects.all()
    return render(request, 'courses/index.html', {'courses':cursos})

def detail(request, pk):
    template_name = 'courses/detail.html'
    context = {'curso': Course.objects.filter(pk=pk)}
    return render(request, template_name, context)
