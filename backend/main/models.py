from django.db import models
from django.conf import settings
from django.core.validators import URLValidator #for URL

def upload_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class Image(models.Model):
    #Django default user model has 
    # 1) first_name, 2) last_name, 3) email, 4) password, 5) is_activate 
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title           = models.CharField(max_length=150)
    image           = models.ImageField(upload_to=upload_image, null=True, blank=True) #Django Store AWS S3
    thumbnail_url   = models.TextField(validators=[URLValidator()])
    privacy         = models.BooleanField(default=False) #False : public; True: private
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)[:50]

    class Meta:
        verbose_name = 'Image Repository'

    """
    @property
    def owner(self):
        return self.user
    """

class Tags(models.Model):
    tagname = models.CharField(max_length=150)
    #images = models.ManyToManyField(Image)

    def __str__(self):
        return str(self.tagname)




