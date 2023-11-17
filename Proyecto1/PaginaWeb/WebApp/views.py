from django.shortcuts import render, HttpResponse

from ServiciosApp.models import Servicio

# Create your views here.

def home(request):

    return render(request, 'WebApp/home.html')


def servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'WebApp/servicios.html', {'ServiciosApp':servicios})


def tienda(request):

    return render(request, 'WebApp/tienda.html')


def blog(request):

    return render(request, 'WebApp/blog.html')


def contacto(request):

    return render(request, 'WebApp/contacto.html')