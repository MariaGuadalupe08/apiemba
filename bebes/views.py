from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Bebe
from .serializers import BebeSerializer

class BebeListView(generics.ListCreateAPIView):
    queryset = Bebe.objects.all()
    serializer_class = BebeSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

class BebeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bebe.objects.all()
    serializer_class = BebeSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación
