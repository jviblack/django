from django.http import HttpResponse
import datetime

def saludo(request):

    docu = """<html><body><h1>

    Hola a todos

    </h1></body></html>"""

    return HttpResponse (docu)

def fecha(request):

    fecha_actual=datetime.datetime.now()

     docu = """<html><body><h1>

    Fecha y hora actuales %s

    </h1></body></html>""" % fecha_actual

    return HttpResponse (docu)
