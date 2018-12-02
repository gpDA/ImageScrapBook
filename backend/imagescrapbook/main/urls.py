
from django.urls import include, path
from .views import ImageAPIView, ImageAPIDetailView

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('<int:id>', ImageAPIDetailView.as_view())
]
