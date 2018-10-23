from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from musicstoreadmin.models import Order
from decimal import Decimal

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        "business": settings.PAYPAL_RECIEVER_EMAIL,
        "amount": "{}".format(order.get_cart_total().quantize(Decimal('.01'))),
        "item_name": "Order {}".format(order.id),
        "invoice": str(order.id),
        "currency_code": 'USD',
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return": 'http://{}{}'.format(host, reverse('payment:done')),
        "cancel_return": 'http://{}{}'.format(host, reverse('payment:canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order':order, 'form':form})
