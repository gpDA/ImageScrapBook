from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('publicgallery'))),
    path('admin', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('main.urls')),
    path('login/', include('login.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('image/', include('image.urls')),
    path('api/', include('registration.urls')),
    path('gallery/', include('gallery_django.urls'))
]
