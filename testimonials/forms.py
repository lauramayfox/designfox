from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'testimonial_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'testimonial_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your testimonial here...'}),
        }
