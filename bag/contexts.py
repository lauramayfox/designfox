def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0

  # Free delivery if over 50, flat rate under
    if product_count > 0:
        if total >= 50: 
            delivery = 0
        else: 
            delivery = 5

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context

