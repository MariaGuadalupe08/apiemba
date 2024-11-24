from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Mama
from .serializers import MamaSerializer

class MamaListView(generics.ListCreateAPIView):
    queryset = Mama.objects.all()
    serializer_class = MamaSerializer
    permission_classes = [AllowAny]  

class MamaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mama.objects.all()
    serializer_class = MamaSerializer
    permission_classes = [AllowAny]  