from django.contrib.sitemaps import Sitemap
from blog.models import post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date