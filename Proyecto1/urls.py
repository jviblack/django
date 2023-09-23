from django.contrib import admin
from django.urls import path

from Proyecto1.views import saludo, fecha, edad

app_name = "autor_app"

urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name="autores"),
    path('saludo/', saludo),
    path('fecha/', fecha),
    path('edades/<int:agno>', edad)
]