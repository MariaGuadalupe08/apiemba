from rest_framework import serializers
from .models import Bebe

class BebeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebe
        fields = ['id', 'imagenBebe', 'descripcionBebe', 'imagenFruta', 'descripcionFruta']
