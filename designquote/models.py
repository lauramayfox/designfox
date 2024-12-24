from django.db import models

class DesignQuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    project_description = models.TextField()
    budget_range = models.CharField(max_length=100)
    timeline = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote request from {self.name}"