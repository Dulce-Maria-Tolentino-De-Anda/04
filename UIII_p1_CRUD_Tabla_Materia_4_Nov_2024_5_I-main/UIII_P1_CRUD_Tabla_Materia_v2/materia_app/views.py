from django.shortcuts import render, redirect
from .models import Materia
# Create your views here.

def inicio_vista(request):
    lasmaterias = Materia.objects.all()
    return render(request, 'gestionarMateria.html', {"mismaterias": lasmaterias})

def registrarMateria(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtmateria']
    credito = request.POST['numcreditos']

    guardarmateria = Materia.objects.create(codigo = codigo, nombre = nombre, credito = credito)
    return redirect("/") 


def seleccionarMateria(request, codigo):
    materia = Materia.objects.get(codigo=codigo)
    return render(request, "editarmateria.html", {"mismaterias": materia})

def editarMateria(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtmateria']
    credito = request.POST['numcreditos']

    materia = Materia.objects.get(codigo=codigo)
    materia.nombre = nombre
    materia.credito = credito
    materia.save()
    return redirect("/") 

def borrarMateria(request, codigo):
    mat = Materia.objects.get(codigo=codigo)
    mat.delete()
    
    return redirect("/")
