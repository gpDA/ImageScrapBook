from django.urls import path
from .views import ImageView, ImageUploadView, ShareView


urlpatterns = [
    path('', ImageUploadView.as_view(template_name="image/imageupload.html"), name="uploadimage"),
    path('<int:pk>', ImageView.as_view(template_name="image/image.html"), name="viewimage"),
    path('<int:img>/share', ShareView.as_view(), name='share')
]
