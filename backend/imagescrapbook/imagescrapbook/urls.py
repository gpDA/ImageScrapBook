from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),
    path('gallery', TemplateView.as_view(template_name="gallery/index.html")),
    path('registration', TemplateView.as_view(template_name="registration/index.html")),
    path('', include('gallery.urls')),
    path('', include('registration.urls')),
]
