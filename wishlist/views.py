from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from products.models import Product 

def wishlist(request):
    # Logic to display the wishlist
    return render(request, 'wishlist/wishlist.html')



def add_to_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
        if created:
            # Optionally, add a success message here
            pass
        return redirect('wishlist:wishlist')  # Add the namespace
    else:
        return redirect('login')
