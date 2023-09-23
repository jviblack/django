from django.http import HttpResponse
import datetime
from django.views.generic.base import RedirectView

def saludo(request):

    docu = """<html><body><h1>

    Hola a todos

    </h1></body></html>"""

    return HttpResponse (docu)

def fecha(request):

    fecha_actual=datetime.datetime.now()

    docu = """<html><body><h2>

    Fecha y hora actuales %s

    </h2></body></html>""" % fecha_actual

    return HttpResponse (docu)

def edades(request, edad, agno):

    #edad_actual=18
    periodo=agno-2023
    edad_futura=edad+periodo
    docu = """<html><body><h2>

    En el año %s tendrás %s años

    </h2></body></html>""" %(agno, edad_futura) 

    return HttpResponse (docu)