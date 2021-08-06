from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_GIFT_THRESHOLD:
        gift = total * Decimal(settings.STANDARD_GIFT_PERCENTAGE / 100)
        free_gift_delta = settings.FREE_GIFT_THRESHOLD - total
    else:
        gift = 0
        free_gift_delta = 0

    grand_total = gift + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'gift': gift,
        'free_gift_delta': free_gift_delta,
        'free_gift_threshold': settings.FREE_GIFT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
