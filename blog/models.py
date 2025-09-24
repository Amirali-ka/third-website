from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class category (models.Model) :
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class post (models.Model):
    image=models.ImageField( upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    tags = TaggableManager()
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    counted_comments = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pid": self.id})
def __str__(self):
        return self.id
class comment (models.Model) :
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject=models.CharField(max_length=250)
    message=models.TextField()
    status = models.BooleanField(default=False)
    login_require=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name