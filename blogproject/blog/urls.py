from django.urls import path,re_path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),

    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # path('post/<int:pk>/', views.detail, name='detail'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),

    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    # path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    path('archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),

    # url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    # path('category/<int:pk>', views.category, name='category'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),

    path('search/', views.search, name='search'),
    path('aa/', views.aa, name='aa'),
]