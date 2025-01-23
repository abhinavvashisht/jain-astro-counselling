from django.shortcuts import render
from .models import Service
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    return render(request, 'blog.html')

def blogdetail(request):
    return render(request, 'blog-detail.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def terms(request):
    return render(request, 'terms-service.html')

def privacypolicy(request):
    return render(request, 'privacy-policy.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services': services})
