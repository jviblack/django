from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'WebApp/home.html')


def servicios(request):

    return render(request, 'WebApp/servicios.html')


def tienda(request):

    return render(request, 'WebApp/tienda.html')


def blog(request):

    return render(request, 'WebApp/blog.html')


def contacto(request):

    return render(request, 'WebApp/contacto.html')