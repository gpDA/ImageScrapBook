
from django.urls import include, path
from .views import SharingAPIView, SharingCreateAPIView

urlpatterns = [
    path('sharing', SharingAPIView.as_view()),
    path('sharing/create', SharingCreateAPIView.as_view()),
    
    
]
