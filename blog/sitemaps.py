from django.contrib.sitemaps import Sitemap
from .models import Blog


class StorySitemap(Sitemap):
    def items(self):
        return Blog.objects.all()
