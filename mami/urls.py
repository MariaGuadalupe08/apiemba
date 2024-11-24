from django.urls import path
from .views import MamaListView, MamaDetailView

urlpatterns = [
    path('mami/', MamaListView.as_view(), name='mama-list'),
    path('mami/<int:pk>/', MamaDetailView.as_view(), name='mama-detail'),
]