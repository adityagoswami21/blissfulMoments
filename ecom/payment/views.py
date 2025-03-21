from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages
# Create your views here.

def process_order(request):
    if request.POST:
        # Get Billing Info from the last page
        payment_form = PaymentForm(request.POST or None)
    else:
        messages.success(request, "Access Denied")
        return redirect('index')

def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        # Check to see if user is logged in
        if request.user.is_authenticated:
            # Get the billing for
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html', {"cart_products":cart_products, "quantities": quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
        else:
            # Not logged in
            # Get the billing for
            billing_form = PaymentForm()
            return render(request, 'payment/billing_info.html', {"cart_products":cart_products, "quantities": quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
        
    else:
        messages.success(request, "Access Denied")
        return redirect('index')


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    if request.user.is_authenticated:
        # Checkout as logged in user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, 'payment/checkout.html', {"cart_products":cart_products, "quantities": quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, 'payment/checkout.html', {"cart_products":cart_products, "quantities": quantities, "totals":totals, "shipping_form":shipping_form})
    

def payment_success(request):
    return render(request, "payment/payment_success.html", {})
