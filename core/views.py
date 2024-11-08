from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber

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