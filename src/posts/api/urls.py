from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='api-list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='api-create'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='api-detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='api-update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='api-delete'),
]