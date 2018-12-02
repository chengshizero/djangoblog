from django.conf.urls import url
from django.urls import path,include
from . import views

app_name = 'comments'
urlpatterns = [
    # url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
    path('comment/post/<int:post_pk>', views.post_comment, name='post_comment'),
]