from django.urls import include, path
from .views import ImageAPIView, ImageAPIDetailView, ImageCreateAPIView, ImageReadAPIView

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('create', ImageCreateAPIView.as_view()),
    path('read', ImageReadAPIView.as_view()),
    path('<int:id>', ImageAPIDetailView.as_view()),
]
