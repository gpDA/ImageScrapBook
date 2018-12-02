
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserAPIView, UserAPIDetailView #UserCreate, 

urlpatterns = [
    #path('user/create', UserCreate.as_view()), #create user
    #jwt
    path('api-token-create', obtain_jwt_token), #obtain token
    path('api-token-refresh', refresh_jwt_token), #refresh token #KEEP THE USER "logged in" the site without having to re-enter their password, or get kicked out by surprise before their token expired
    path('api-token-verify', verify_jwt_token),

    #token authenticaiton vs. rest=auth get key by logging in

    #login / logout
    # login : rest-auth/login
    # logout : rest-auth/logout
    path('rest-auth/', include('rest_auth.urls')),

    
    path('user', UserAPIView.as_view()),
    path('user/<int:id>', UserAPIDetailView.as_view()),
]
