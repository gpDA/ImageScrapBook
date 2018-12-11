from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from .views import GalleryView, SharedWithView


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('publicgallery'))),
    path('<int:pk>', GalleryView.as_view(template_name='gallery/gallery.html'), name='gallery'),
    path('public', GalleryView.as_view(template_name='gallery/gallery.html'), name='publicgallery'),
    path('shared', SharedWithView.as_view(), name='sharedgallery')
]
