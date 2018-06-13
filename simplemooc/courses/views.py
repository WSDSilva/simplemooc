from django.shortcuts import render, get_object_or_404
from .models import Course 

def index(request):
    cursos = Course.objects.all()
    return render(request, 'courses/index.html', {'courses':cursos})

#def detail(request, pk):
#    template_name = 'courses/details.html'
#    context = {'curso': Course.objects.get(pk=pk)}
#    return render(request, template_name, context)

def detail(request, slug):
    template_name = 'courses/details.html'
    course = get_object_or_404(Course, slug=slug)
    context = {'curso': course}
    return render(request, template_name, context)
