from django import template
from django.utils import timezone
from blog.models import post
register=template.Library()

@register.inclusion_tag('lastest_post.html')
def lastestposts(x):
     posts = post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')        
     posts.reverse()              
     posts = posts[:x] 
     return {'posts':posts}