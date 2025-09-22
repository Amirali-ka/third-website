from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',blog_view,name='blog'),
    path('post-<int:pid>',blog_detail_view,name='blog-detail'),
    path('search/',blog_search ,name='search'),
    path('tag-<str:tag_str>',blog_tags ,name='tag'),
    path('category-<str:cat_str>',blog_category ,name='category'),
]