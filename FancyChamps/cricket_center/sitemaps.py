from django.contrib.sitemaps import Sitemap
#from FancyChamps.urls import urlpatterns as FancyChampsUrls
from django.core.urlresolvers import reverse

class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.

    def items(self):
        return ['IndexView', 'about_us', 'privacy_policy', 'terms', 'how_to_play', 'points_system', 'faqs',]

    def location(self, item):
        return reverse(item)