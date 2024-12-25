from django.urls import path
from . import views

app_name = 'wishlist'  # Register the namespace for the wishlist app

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('', views.wishlist, name='wishlist'),  # Add a route for the wishlist view
]