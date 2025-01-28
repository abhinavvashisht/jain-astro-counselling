from django.shortcuts import render, redirect
from .models import Service, Testimonial, TeamMember
from .forms import TestimonialForm, TeamMemberForm
# Create your views here.

def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html',{'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def team(request):
    team_members = TeamMember.objects.filter(is_active=True).order_by('name')
    return render(request, 'team.html',{'team_members': team_members})

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
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html',{'testimonials': testimonials})

def terms(request):
    return render(request, 'terms-service.html')

def privacypolicy(request):
    return render(request, 'privacy-policy.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services': services})

def services_detail(request):
    services = Service.objects.all()
    return render(request, 'services-detail.html',{'services': services})

def add_testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonials')  # Redirect to the testimonials page after submission
    else:
        form = TestimonialForm()

    return render(request, 'add_testimonial.html', {'form': form})

def add_team_member(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team')  # Redirect to the team page or any other page
    else:
        form = TeamMemberForm()

    return render(request, 'add_team_member.html', {'form': form})
