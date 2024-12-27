from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'submitted_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected testimonials have been approved.")
    approve_testimonials.short_description = "Approve selected testimonials"
