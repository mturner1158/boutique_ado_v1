from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_conunt = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delviery = 0 
        free_delivery_delta = 0 

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_conunt,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threashold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context