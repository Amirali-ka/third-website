from django.urls import path
from mysite.views import *

app_name = 'mywebsite'

urlpatterns = [
    path('',index_view,name='index'),
    path('contact/',contact_view,name='contact'),
    path('about/',about_view,name='about'),
]