
from django.urls import include, path
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import RegisterView, UserAPIDetailView, UserAPIView
from django.conf import settings
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    #path('user/create', UserCreate.as_view()), #create user
    #jwt
    # path('api-token-create', obtain_jwt_token), #obtain token
    # path('api-token-refresh', refresh_jwt_token), #refresh token #KEEP THE USER "logged in" the site without having to re-enter their password, or get kicked out by surprise before their token expired
    # path('api-token-verify', verify_jwt_token),

    #token authenticaiton vs. rest=auth get key by logging in

    #login / logout
    # login : rest-auth/login
    # logout : rest-auth/logout
    path('rest-auth/', include('rest_auth.urls')), #https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html

    path('rest-auth/registration', RegisterView.as_view(), name='rest_register'),
    
    path('get_auth_token', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('obtain_token_auth', rest_framework_views.obtain_auth_token, name='get_auth_token'),

    path('user', UserAPIView.as_view()),

    path('user/<slug:username>', UserAPIDetailView.as_view()),
]
