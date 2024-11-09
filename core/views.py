from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

def index(request):
    return render(request, 'core/index.html')

def content(request):
    return render(request, 'core/content.html')

def system(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            NewsletterSubscriber.objects.create(email=email)
            messages.success(request, 'Successfully subscribed to our newsletter!')
        except:
            messages.error(request, 'This email is already subscribed.')
        return redirect('core:system')
    return render(request, 'core/system.html')

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['core:index', 'core:content', 'core:system']

    def location(self, item):
        return reverse(item)

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /private/",
        "Allow: /",
        "Sitemap: https://thelabmena.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")