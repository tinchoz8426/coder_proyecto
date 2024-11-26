from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "app_coder/index.html")

def cursos(request):
    return render(request, "app_coder/cursos.html")

def profesores(request):
    return HttpResponse("vista profesores")

def estudiantes(request):
    return HttpResponse("vista estudiantes")

def entregables(request):
    return HttpResponse("vista entregables")