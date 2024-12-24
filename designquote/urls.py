from django.urls import path
from . import views

urlpatterns = [
    path('quote-request/', views.design_quote_request, name='design_quote_request'),
    path('quote-thank-you/', views.quote_thank_you, name='quote_thank_you'),
]