from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from main.models import Image, Sharing
import thumbnail
import uuid
import boto3


class ShareView(LoginRequiredMixin, CreateView):
    model = Sharing
    template_name = 'image/share.html'
    fields = ['shared_to']

    def get_context_data(self, **kwargs):
        kwargs['image'] = Image.objects.get(id=self.kwargs['img'])
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shared_by = self.request.user
        obj.image = Image.objects.get(id=self.kwargs['img'])
        obj.save()
        return HttpResponseRedirect(obj.image.get_absolute_url())


class ImageUploadView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'image']

    def form_valid(self, form):
        obj = Image()
        obj.user = self.request.user
        ext = self.request.FILES['image'].name
        obj.title = form.cleaned_data['title']
        s3 = boto3.resource('s3', use_ssl=False, endpoint_url='http://minio:9000')
        imguuid = uuid.uuid4()
        imgurl = f'{obj.user.id}-{imguuid}.{ext}'
        s3.Object('image', imgurl).put(Body=self.request.FILES['image'])
        obj.imageurl = imgurl
        obj.save()
        thumbnail.thumbnailify.delay(obj.id, imgurl, (200, 200))
        return HttpResponseRedirect(obj.get_absolute_url())


class ImageView(DetailView):
    model = Image
    template_name = 'image/image.html'
