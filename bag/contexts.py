from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for option, quantity in item_data['items_by_option'].items():
                total += quantity * product.price
                count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'option': option,
                })

    if total < settings.FREE_GIFT_THRESHOLD:
        gift = total * Decimal(
                settings.STANDARD_GIFT_PERCENTAGE / 100)
        free_gift_delta = settings.FREE_GIFT_THRESHOLD - total
    else:
        gift = 0
        free_gift_delta = 0

    grand_total = gift + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'count': count,
        'gift': gift,
        'free_gift_delta': free_gift_delta,
        'free_gift_threshold': settings.FREE_GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
