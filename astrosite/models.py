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