from AppCoder.models import Familiar
from django.http import HttpResponse
from django.template import Template, loader

def saludo(request):
    nom = 'Peppa'
    ap = 'Pig'
    diccionario = { "nombre": nom, "apellido": ap}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregarPadre(request):
    plantilla = loader.get_template('template1.html')
    padre = Familiar(nombre="Miguel", apellido="Chávez", edad=59, fechaNacimiento="1963-01-10")
    diccionario = {"nombre": padre.nombre, "apellido": padre.apellido, "edad": padre.edad, "fechaNacimiento": padre.fechaNacimiento}
    padre.save()
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregarMadre(request):
    plantilla = loader.get_template('template1.html')
    padre = Familiar(nombre="Lili", apellido="Loera", edad=51, fechaNacimiento="1971-10-30")
    diccionario = {"nombre": padre.nombre, "apellido": padre.apellido, "edad": padre.edad, "fechaNacimiento": padre.fechaNacimiento}
    padre.save()
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def agregarHermana(request):
    plantilla = loader.get_template('template1.html')
    padre = Familiar(nombre="Angelica", apellido="Gutierrez", edad=22, fechaNacimiento="1999-10-12")
    diccionario = {"nombre": padre.nombre, "apellido": padre.apellido, "edad": padre.edad, "fechaNacimiento": padre.fechaNacimiento}
    padre.save()
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)