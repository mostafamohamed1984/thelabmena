from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'services', 'contact']

    def location(self, item):
        return reverse(item)

class ServicesSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['digital-marketing-kuwait', 'digital-marketing-lebanon', 
                'seo-services', 'social-media-marketing']

    def location(self, item):
        return f'/services/{item}/' 

class LocationSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return [
            'digital-marketing-kuwait-city',
            'digital-marketing-lebanon-beirut',
            'seo-services-kuwait',
            'seo-services-lebanon',
            'social-media-marketing-kuwait',
            'social-media-marketing-lebanon',
            'web-development-mena',
            'branding-agency-middle-east'
        ]

    def location(self, item):
        return f'/services/{item}/'