from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
  

    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='capi-list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='capi-create'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='capi-thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]