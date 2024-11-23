from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse 
from django.conf.urls.static import static

def home(request): 
    return HttpResponse("Bienvenido a la API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('exercises.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
