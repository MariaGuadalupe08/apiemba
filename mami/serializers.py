from rest_framework import serializers
from .models import Mama

class MamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mama
        fields = ['id', 'descripcionMama', 'imagenSintoma', 'descripcionSintoma']