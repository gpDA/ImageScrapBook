
from django.conf.urls import url
from .views import ImageAPIView, ImageAPIDetailView

urlpatterns = [
    url(r'^$', ImageAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ImageAPIDetailView.as_view()),
]
