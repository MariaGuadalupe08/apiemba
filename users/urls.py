from django.urls import path
from .views import RegisterView, LoginView, UserDetailView
from .views import UserIDView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user-id/<str:username>/', UserIDView.as_view(), name='user-id'),
]
