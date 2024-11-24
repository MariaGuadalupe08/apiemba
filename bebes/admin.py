from django.contrib import admin
from .models import Bebe

@admin.register(Bebe)
class BebeAdmin(admin.ModelAdmin):
    list_display = ('descripcionBebe', 'descripcionFruta')
