from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "Theres nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51UUQdgR0ceews76jdF0tWK2pGCQDvpiKWS7OvXxEOKh5d9oiZaBoLx7WRTTbOOtqB97XKNEom8HVaYuhcHpJXB3F00P44Zk60m',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
