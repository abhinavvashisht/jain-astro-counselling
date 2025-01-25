from django import forms
from .models import Testimonial, TeamMember

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

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = [
            'name',
            'role',
            'email',
            'phone_number',
            'expertise',
            'qualification',
            'short_description',
            'is_active',
        ]
        widgets = {
            'date_joined': forms.DateInput(attrs={'type': 'date'}),
            'short_description': forms.Textarea(attrs={'rows': 3}),
        }