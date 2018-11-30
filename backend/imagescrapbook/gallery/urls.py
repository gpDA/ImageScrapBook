from django.conf.urls import url
from . import views

urlpatterns = [
    url('gallery', views.index),
]