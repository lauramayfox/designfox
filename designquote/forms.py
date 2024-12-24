from django import forms
from .models import DesignQuoteRequest

class DesignQuoteRequestForm(forms.ModelForm):
    class Meta:
        model = DesignQuoteRequest
        fields = ['name', 'email', 'phone_number', 'project_description', 'budget_range', 'timeline']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 4}),
        }