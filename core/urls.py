from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap

app_name = 'core'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Main template URLs
    path('', views.index, name='index'),
    path('content/', views.content, name='content'),
    path('system/', views.system, name='system'),
    
    # Core template URLs
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]