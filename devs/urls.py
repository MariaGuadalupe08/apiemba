from django.urls import path
from .views import DevListView, DevDetailView

urlpatterns = [
    path('devs/', DevListView.as_view(), name='dev-list'),
    path('devs/<int:pk>/', DevDetailView.as_view(), name='dev-detail'),
]
