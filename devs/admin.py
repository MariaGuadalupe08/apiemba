from django.contrib import admin
from .models import Dev

@admin.register(Dev)
class DevAdmin(admin.ModelAdmin):
    list_display = ('nombredev', 'apellidodev', 'numerodev', 'nocontroldev', 'correoddev')
