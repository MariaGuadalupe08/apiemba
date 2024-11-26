from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import Dev
from .serializers import DevSerializer

class DevListView(generics.ListCreateAPIView):
    queryset = Dev.objects.all()
    serializer_class = DevSerializer
    permission_classes = [AllowAny]

class DevDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dev.objects.all()
    serializer_class = DevSerializer
    permission_classes = [AllowAny]
