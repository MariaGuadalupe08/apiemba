from django.contrib import admin
from .models import Mama

@admin.register(Mama)
class MamaAdmin(admin.ModelAdmin):
    list_display = ('descripcionMama', 'descripcionSintoma')