from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    product_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        product_total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if product_total < settings.FREE_GIFT_THRESHOLD:
        gift = product_total * Decimal(
                settings.STANDARD_GIFT_PERCENTAGE / 100)
        free_gift_delta = settings.FREE_GIFT_THRESHOLD - product_total
    else:
        gift = 0
        free_gift_delta = 0

    grand_total = gift + product_total

    context = {
        'bag_items': bag_items,
        'product_total': product_total,
        'product_count': product_count,
        'gift': gift,
        'free_gift_delta': free_gift_delta,
        'free_gift_threshold': settings.FREE_GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
