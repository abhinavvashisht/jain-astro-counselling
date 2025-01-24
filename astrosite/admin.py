from django.contrib import admin
from .models import Service, Testimonial

# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')
    search_fields = ('service',)
    list_filter = ('price',)
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'created_at')
    search_fields = ('name', 'message', 'designation')