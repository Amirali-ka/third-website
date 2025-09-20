from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage
from django.utils import timezone
from blog.models import post,comment
from blog.forms import commentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def blog_view(request):
    posts=post.objects.filter(published_date__lte=timezone.now(),status=1)
    return render(request,'blog.html',{'posts':posts})
def blog_detail_view(request,pid):
    t=comment.objects.filter(post=pid).count()
    posts=get_object_or_404(post,pk=pid,published_date__lte=timezone.now(),status=1)
    posts.counted_views+=1
    posts.counted_comments=t
    posts.save()
    postss=post.objects.filter(published_date__lte=timezone.now(),status=1)
    try:
        prev_post = post.objects.filter(published_date__lte=timezone.now(),status=1,pk__lt=pid).order_by('-pk').first()
    except post.DoesNotExist:
        prev_post = None

    try:
        next_post = post.objects.filter(published_date__lte=timezone.now(),status=1,pk__gt=pid).order_by('pk').first()
    except post.DoesNotExist:
        next_post = None
        
    comments=comment.objects.filter(post=pid).order_by('created_date')
    if request.method=='POST':
        form=commentform(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = posts
            new_comment.save()
            messages.add_message(request,messages.SUCCESS,'your submit is successful')
        else:
           messages.add_message(request,messages.ERROR,'your submit is not successful')
    else:
        form=commentform()
    comments=comment.objects.filter(post=posts).order_by('created_date')
    dict={'posts':posts,'next':next_post,'prev':prev_post,'comments':comments,'form':form,'postss':postss}
    return render(request,'blog_detail.html',dict)

