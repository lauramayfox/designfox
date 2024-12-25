from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from products.models import Product 

def wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
        return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})
    else:
        return redirect('login')


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


def remove_from_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        Wishlist.objects.filter(user=request.user, product=product).delete()
        return redirect('wishlist:wishlist')
    else:
        return redirect('login')

