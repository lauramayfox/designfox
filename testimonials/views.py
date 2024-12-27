from django.shortcuts import render, redirect
from .forms import TestimonialForm
from .models import Testimonial
from django.contrib import messages

def testimonial_list(request):
    # Handle form submission
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for submitting your testimonial!")
            return redirect('thank_you') 
    else:
        form = TestimonialForm()

    # Get approved testimonials
    testimonials = Testimonial.objects.filter(approved=True).order_by('-submitted_at')
    
    # Render the template with the form and testimonials
    return render(request, 'testimonials/testimonial_list.html', {
        'form': form,
        'testimonials': testimonials,
    })


def thank_you(request):
    return render(request, 'testimonials/thank_you.html')