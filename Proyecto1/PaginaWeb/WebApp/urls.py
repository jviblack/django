from django.urls import path

from WebApp import views 

urlpatterns = [
    #path('admin/', admin.site.urls), está en el urls.py de la paginaweb
    path('', views.home, name="Home"),
    path('servicios/', views.servicios, name="Servicios"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
]