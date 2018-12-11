from django.urls import path
from django.contrib.auth import views as authviews
from .views import SignupView, Login


urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('signup', SignupView.as_view(), name='signup'),
]
