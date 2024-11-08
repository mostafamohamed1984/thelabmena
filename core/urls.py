from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Main template URLs
    path('', views.index, name='index'),
    path('content/', views.content, name='content'),
    path('system/', views.system, name='system'),
    
    # Core template URLs
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]