from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/service_images/')

    def __str__(self):
        return self.service
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # Name of the person giving the testimonial
    message = models.TextField()  # Testimonial message
    designation = models.CharField(max_length=100, blank=True, null=True)  # Optional designation
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Optional photo
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the testimonial was added

    def __str__(self):
        return self.name
    
class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('counselor', 'Counselor'),
        ('manager', 'Manager'),
        ('support', 'Support Staff'),
        ('admin', 'Administrator'),
    ]

    name = models.CharField(max_length=100, help_text="Full name of the team member")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, help_text="Role in the team")
    email = models.EmailField(unique=True, help_text="Email address")
    phone_number = models.CharField(max_length=15, help_text="Contact phone number")
    expertise = models.TextField(blank=True, help_text="Areas of expertise or specialization")
    qualification = models.CharField(max_length=255, blank=True, help_text="Qualifications of the team member")
    short_description = models.TextField(blank=True, help_text="A brief description of the team member")
    date_joined = models.DateField(auto_now_add=True, help_text="Date the team member joined")
    is_active = models.BooleanField(default=True, help_text="Is the team member currently active?")

    def __str__(self):
        return f"{self.name} ({self.role})"

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['name']
