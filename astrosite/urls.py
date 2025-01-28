from django.urls import path
from .import views
from .views import add_testimonial_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services-detail/', views.services_detail, name='services_detail'),
    path('team/', views.team, name='team'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogdetail, name='blogdetail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('terms-service/', views.terms, name='terms'),
    path('privacy-policy/', views.privacypolicy, name='privacypolicy'),
    path('add-testimonial/', add_testimonial_view, name='add_testimonial'),
    path('add-team-member/', views.add_team_member, name='add_team_member'),
]
