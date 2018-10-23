from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib import messages

from musicstoreadmin.models import Product, Category, OrderItem, Order
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from store.forms import SignUpForm
from store.extras import generate_order_id, get_item_count, cart_total_price
import datetime

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products' : product,
        'count' : get_item_count(),
        'categories' : category
    }
    return render(request, 'store/index.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    return render(request, 'store/product.html', {'product':product, 'count':get_item_count()})

def checkout(request):
    cart_item = OrderItem.objects.all()
    #cart mngmnt
    #payment rqst
    if request.method == 'POST':
        order = Order.objects.create(OR = generate_order_id(),
                             is_ordered = True,
                             order_date = datetime.datetime.now(),
                             raw_total_price = cart_total_price())
        order.items.set(cart_item)
        request.session['order_id'] = order.id
        return redirect(reverse('payment:process'))
    context = {
        'cart_items' : cart_item,
        'count' : get_item_count(),
        'total_price' : cart_total_price()
    }
    return render(request, 'store/checkout.html', context)

def signupsuccess(request):
    return render(request,'store/signupsuccess.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('store:signupsuccess'))
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form' : form, 'count' : get_item_count()})

def add_to_cart(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if product.number_of_stocks > 0:
        order_item, status = OrderItem.objects.get_or_create(product=product)
        user_order, status = Order.objects.get_or_create(OR = generate_order_id())
        user_order.items.add(order_item)
        product.number_of_stocks -= 1
        product.save()
        user_order.save()
    else:
        messages.info(request, 'Item currently out of stock')
    return redirect(reverse('store:index'))

def delete_cart_item(request, item_id):
    OrderItem.objects.filter(id=item_id).delete()
    return redirect(reverse('store:checkout'))
