
from django.urls import include, path
from .views import ImageAPIView, ImageAPIDetailView, UserCreate, UserAPIView

urlpatterns = [
    path('user/create', UserCreate.as_view()),
    path('user', UserAPIView.as_view()),
    path('', ImageAPIView.as_view()),
    path('<int:id>', ImageAPIDetailView.as_view())
]
