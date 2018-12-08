from django.db import models
from django.conf import settings
from django.core.validators import URLValidator


def upload_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class Image(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title           = models.CharField(max_length=150)
    image           = models.ImageField(upload_to=upload_image, null=True, blank=True) # dummy for forms
    extension       = models.CharField(max_length=10) # likewise
    imageurl        = models.TextField(blank=True, default='')
    #thumanail 1) PROCESSING? 2) SAVED?
    thumbnail_url   = models.TextField(validators=[URLValidator()], blank=True, default='')
    privacy         = models.BooleanField(default=False) #False : public; True: private
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)[:50]

    class Meta:
        verbose_name = 'Image Repository'



class Sharing(models.Model):
    shared_to            = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_shared_to', on_delete=models.CASCADE)    
    shared_by            = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_shared_by', on_delete=models.CASCADE)
    Image                = models.ForeignKey(Image, on_delete=models.CASCADE)    


class Tag(models.Model):
    tagname           = models.CharField(max_length=150)
    images          = models.ManyToManyField(Image)

    def __str__(self):
        return str(self.tagname)