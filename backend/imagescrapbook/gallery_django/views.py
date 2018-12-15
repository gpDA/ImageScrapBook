from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from main.models import Image, Sharing

class SharedWithView(LoginRequiredMixin, ListView):
    model = Sharing
    template_name = 'gallery/sharedgallery.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(shared_to=self.request.user.id)

    def get_context_data(self, **kwargs):
        kwargs['gallerytype'] = 'share'
        kwargs['user'] = self.request.user
        return super().get_context_data(**kwargs)


class GalleryView(ListView):
    model = Image
    template_name = 'gallery/gallery.html'
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset()
        if 'pk' in self.kwargs:
            qs = qs.filter(user=self.kwargs['pk'])
        else:
            qs = qs.filter(privacy=False)
        return qs.order_by('-timestamp')

    def get_context_data(self, **kwargs):
        if 'pk' in self.kwargs:
            kwargs['gallerytype'] = "user"
            kwargs['username'] = User.objects.get(pk=self.kwargs['pk']).username
        else:
            kwargs['gallerytype'] = "public"
        return super().get_context_data(**kwargs)
