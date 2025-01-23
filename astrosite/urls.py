from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('terms-service/', views.terms, name='terms'),
    path('privacy-policy/', views.privacypolicy, name='privacypolicy'),
]
