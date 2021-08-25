from django.shortcuts import render
import json
import os
from .models import Product, ProductCategory


# Create your views here.

def index(request):
    data = {'title': 'GeekSHOP'}
    return render(request, 'products/index.html', context=data)


def products(request):
    data = dict()
    data['title'] = 'GeekPRODUCTS'
    data['category_list'] = ProductCategory.objects.all()
    data['product_list'] = Product.objects.all()
    return render(request, 'products/products.html', context=data)
