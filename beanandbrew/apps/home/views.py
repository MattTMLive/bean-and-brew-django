from django.shortcuts import render
from .models import *
from .forms import *
from django.db import connection
import datetime

# Create your views here.
from django.views.generic import View


class home_page(View):

    def get(self, request):
        return render(request, 'home/index.html')

class products_page(View):

    def get(self, request):
        products = Product.objects.raw('SELECT * FROM products')

        return render(request, 'home/products.html', {"products": products})

class order_page(View):

    def get(self, request):
        products = Product.objects.raw('SELECT * FROM products')

        return render(request, 'home/order.html', {"products": products})

    def post(self, request):
        form = OrderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            cursor = connection.cursor()
            try:
                cursor.execute(f"INSERT INTO orders (name, order_time, status, coffee_id) VALUES ('{data['name']}', '{datetime.datetime.now().isoformat()}', 0, {data['coffee']})")
            except Exception as e:
                raise e
        else:
            print(form.errors)


        return self.get(request)