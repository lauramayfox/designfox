from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

from django.shortcuts import render, redirect

def add_to_bag(request, item_id):
    """ Add the specified product to the shopping bag with a default quantity of 1 """
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Increment quantity if product already in the bag, else add it with quantity 1
    if item_id in bag:
        bag[item_id] += 1
    else:
        bag[item_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)
