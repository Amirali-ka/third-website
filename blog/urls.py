from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('post-<int:pid>',blog_detail_view,name='blog-detail'),
]