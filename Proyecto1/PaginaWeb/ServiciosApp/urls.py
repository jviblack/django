from django.urls import path

from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls), está en el urls.py de la paginaweb
    #path('', views.home, name="Home"),
    path('', views.servicios, name="Servicios"),
    #path('tienda/', views.tienda, name="Tienda"),
    #path('blog/', views.blog, name="Blog"),
    #path('contacto/', views.contacto, name="Contacto"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)