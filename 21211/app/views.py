from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.models import Order


def checkout(request, order_pk):
    o = get_object_or_404(Order, id=order_pk)
    items = o.orderitem_set.all()
    total_price = 0
    # TODO: calculation does not work for some fucking reason!
    for item in items:
        total_price += item.product.price * item.quantity
    res = "{:.2f}".format(total_price)
    return HttpResponse({"total_price": res})
