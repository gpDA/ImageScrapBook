from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),


    path('gallery', TemplateView.as_view(template_name="gallery/public.html")),
    path('gallery111', TemplateView.as_view(template_name="gallery/private.html")), #need to be gallery/<userId>

    path('signup', TemplateView.as_view(template_name="registration/signup.html"), name='signup'),    
    path('login', TemplateView.as_view(template_name="registration/login.html"),name='login'),    
    path('logout', TemplateView.as_view(template_name="registration/logout.html"),name='logout'),    
    
    path('', include('gallery.urls')),
    path('', include('registration.urls')),
]
