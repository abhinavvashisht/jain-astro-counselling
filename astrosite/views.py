from django.shortcuts import render
from .models import Service
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services': services})
