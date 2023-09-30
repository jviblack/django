from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import Formulario_Contacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")


def buscar(request):

    if request.GET["prd"]:

        #mensaje="Artículo buscado: %r" % request.GET["prd"]
        producto=request.GET["prd"]

        if len(producto)>20:

            mensaje = "Texto demasiado largo"

        else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:

        mensaje="No has introducido nada"

    return HttpResponse(mensaje)


def contacto(request):

    # if request.method=="POST":

    #     subject=request.POST["ASUNTO"]
    #     message=request.POST["MENSAJE"] + " " + request.POST["EMAIL"]
    #     email_from=settings.EMAIL_HOST_USER
    #     recipient_list=["javie.couto.dominguez@gmail.com"]
    #     send_mail(subject, message, email_from, recipient_list)

    #     return render(request, "gracias.html")

    if request.method=="POST":

        mi_formulario=Formulario_Contacto(request.POST)

        if mi_formulario.is_valid():

            info=mi_formulario.cleaned_data

            send_mail(info['asunto'], info['mensaje'], info.GET('email', 'javie.couto.dominguez@gmail.com'),
                       ['javie.couto.dominguez@gmail.com'],)

            return render(request, "gracias.html")
        
    else:

        mi_formulario=Formulario_Contacto()

    return render(request, "formulario_contacto.html", {"form":mi_formulario})
