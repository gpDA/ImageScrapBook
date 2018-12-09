
from django.urls import include, path
from .views import SharingAPIView

urlpatterns = [
    path('sharing', SharingAPIView.as_view()),
    
    
]
