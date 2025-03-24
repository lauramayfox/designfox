from django import forms
from .models import DesignQuoteRequest
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class DesignQuoteRequestForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^\+?\d{7,15}$',
        message=_("Enter a valid phone number (7-15 digits, optional '+').")
    )

    budget_validator = RegexValidator(
        regex=r'^\$?\d+(\s*-\s*\$?\d+)?$|^\d+(\s*-\s*\d+)?$|^\w+$',
        message=_("Enter a valid budget (e.g., '500', '500-1000', or 'five hundred').")
    )

    timeline_validator = RegexValidator(
        regex=r'^\d+\s*(days?|weeks?|months?)$|^\w+\s*(days?|weeks?|months?)$',
        message=_("Enter a valid timeline (e.g., '10 days', '3 weeks', or 'two months').")
    )

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

    phone_number = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Enter your phone number'
        })
    )

    budget_range = forms.CharField(
        validators=[budget_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Enter your budget range'
        })
    )

    timeline = forms.CharField(
        validators=[timeline_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'width: 50%;',
            'placeholder': 'Enter your timeline'
        })
    )
