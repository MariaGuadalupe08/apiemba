from django.urls import path
from .views import BebeListView, BebeDetailView

urlpatterns = [
    path('bebes/', BebeListView.as_view(), name='bebe-list'),
    path('bebes/<int:pk>/', BebeDetailView.as_view(), name='bebe-detail'),
]
