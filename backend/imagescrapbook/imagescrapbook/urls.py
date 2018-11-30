from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', include('rest_framework.urls')),    
    path('', include('main.urls')),
    path('', include('gallery.urls')),
    path('', include('registration.urls')),
]
