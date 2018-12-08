
from django.urls import include, path
from .views import ImageAPIView, ImageAPIDetailView, TagAPIView, SharingAPIView

urlpatterns = [
    path('', ImageAPIView.as_view()),
    path('<int:id>', ImageAPIDetailView.as_view()),
    path('tags/', TagAPIView.as_view()),
    path('sharing/', SharingAPIView.as_view()),
    
]
