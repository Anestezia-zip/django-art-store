from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OJuvzDLZ8UGOw3ldy81W2T7WRoSaxlMlF4AaatOtz73zi7xlUgDL7xaEdhJsd9d59ys6k3QVi3Yq11qs9jkfBa4003VOoQVkl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)