from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, help_text="Only approved testimonials will be displayed.")

    def __str__(self):
        return f"Testimonial from {self.name}"