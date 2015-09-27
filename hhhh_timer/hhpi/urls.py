from django.conf.urls import url

from . import views

urlpatterns = [
    # Current status of riders
    url(r'^$', views.index, name='index'),
    url(r'^/checkpoint/$', views.checkpoint, name='checkpoint'),
]