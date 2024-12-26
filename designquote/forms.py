from django import forms
from .models import DesignQuoteRequest

class DesignQuoteRequestForm(forms.ModelForm):
    class Meta:
        model = DesignQuoteRequest
        fields = ['name', 'email', 'phone_number', 'project_description', 'budget_range', 'timeline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 50%;', 'placeholder': 'Enter your email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;', 'placeholder': 'Enter your phone number'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 50%;', 'rows': 4, 'placeholder': 'Describe your project'}),
            'budget_range': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;', 'placeholder': 'Enter your budget range'}),
            'timeline': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 50%;', 'placeholder': 'Enter your timeline'}),
        }
