from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message', 'designation', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your testimonial'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your designation'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
