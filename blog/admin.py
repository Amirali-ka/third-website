from django.contrib import admin
from blog.models import post,category,comment
from mywebsite.models import Contact,newsletter

# Register your models here.
class postadmin(admin.ModelAdmin):
    date_hierarchy='published_date'
    empty_value_display='-empty-'
    list_display=('title','counted_views','author','status','published_date','created_date')
    list_filter=('status','author')
    search_fields=['title','content']
class commentadmin(admin.ModelAdmin):
    pass
admin.site.register(post,postadmin)
admin.site.register(category)
admin.site.register(Contact)
admin.site.register(newsletter)
admin.site.register(comment,commentadmin)