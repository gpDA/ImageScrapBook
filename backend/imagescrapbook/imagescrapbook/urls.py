from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),
    path('login/', include('login.urls')),
    path('logout', TemplateView.as_view(template_name="registration/logout.html"), name='logout'),
    path('image/', include('image.urls')),
    path('api/', include('registration.urls')),
]
