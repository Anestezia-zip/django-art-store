from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for item_id in bag:
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        bag_items.append({
            'item_id': item_id,
            'product': product,
        })


    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context