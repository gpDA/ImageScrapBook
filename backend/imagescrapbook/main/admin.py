from django.contrib import admin
from main.models import Image

class MainAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image', 'thumbnail_url']

admin.site.register(Image, MainAdmin)