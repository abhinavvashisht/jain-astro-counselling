from django.contrib import admin
from .models import Service, Testimonial, TeamMember

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
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone_number', 'is_active')
    list_filter = ('role', 'is_active', 'date_joined')
    search_fields = ('name', 'email', 'phone_number')
    ordering = ('name',)