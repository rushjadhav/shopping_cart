import ast
import string
import random
import simplejson as json

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.models import User

from models import Category, Product, Order, ProductOrderMap

class IndexView(View):

    def get(self, request):
        products = Product.objects.filter(status='A')[:5]
        return render(request, 'index.html', {'products': products})

class CategoriesView(View):

    def get(self, request):
        categories = Category.objects.filter(status='A')
        json_data = json.dumps([{'name': c.name, 'description': c.description, 'id': c.id,
                                 'productCount': c.products.filter(status='A').count()} for c in categories])
        return HttpResponse(json_data)

class ProductsView(View):

    def get(self, request, category_id):
        json_data = json.dumps([{'name': p.name, 'description': p.description, 'id': p.id,
            'image': p.image.url, 'price': p.price,} for p in Product.objects.filter(category_id=category_id, status='A')], use_decimal=True)
        return HttpResponse(json_data)

class PlaceOrderView(View):

    def get(self, request):
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        user = create_user(first_name, last_name, email)
        order = create_order(user, request.GET.get('address'))

        products = request.GET.getlist('procucts')
        for product in products:
            product = ast.literal_eval(product)
            ProductOrderMap.objects.create(product_id=product['id'],
                                           quantity=product['quantity'],
                                           order=order)
        return HttpResponse('Ok')

def create_user(first_name, last_name, email):
    username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    user = User.objects.create(username=username, first_name=first_name,
                               last_name=last_name,
                               email=email)
    return user

def create_order(user, shipping_address):
    order = Order.objects.create(user=user, shipping_address = shipping_address)
    return order
