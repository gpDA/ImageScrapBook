
from django.urls import include, path
from .views import UserCreate, UserAPIView, UserAPIDetailView

urlpatterns = [
    path('user/create', UserCreate.as_view()),
    path('user', UserAPIView.as_view()),
    path('user/<int:id>', UserAPIDetailView.as_view()),
]
