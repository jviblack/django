from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

from django.views.generic.base import RedirectView

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        pass

def saludo(request):

    p1=Persona("Javi", "Couto")
    #nombre = "Javi"
    #apellido = "Couto"

    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistsa", "Despliegue"]

    ahora = datetime.datetime.now()

    #doc_externo = open("C:/Users/javier.couto/django/Proyecto1/Proyecto1/Proyecto1/templates/template1.html") 
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #ctx = Context({"nombre_yo":p1.nombre, "apellido_yo":p1.apellido, "momento_actual":ahora, "temas":temas_curso})

    #doc_externo = get_template('template1.html')
    #docu = doc_externo.render({"nombre_yo":p1.nombre, "apellido_yo":p1.apellido, "momento_actual":ahora, "temas":temas_curso})

    return render(request, "template1.html", {"nombre_yo":p1.nombre, "apellido_yo":p1.apellido, "momento_actual":ahora, "temas":temas_curso})

    #return HttpResponse(docu)


def cursoPy(request):

    fecha_actual = datetime.datetime.now()

    return render(request, "cursoPy.html", {"fecha_actual":fecha_actual})


def fecha(request):

    fecha_actual = datetime.datetime.now()

    docu = """<html><body><h2>

    Fecha y hora actuales %s

    </h2></body></html>""" % fecha_actual

    return HttpResponse(docu)

def edades(request, edad, agno):

    #edad_actual=18
    periodo=agno-2023
    edad_futura=edad+periodo
    docu = """<html><body><h2>

    En el año %s tendrás %s años

    </h2></body></html>""" %(agno, edad_futura) 

    return HttpResponse(docu)
