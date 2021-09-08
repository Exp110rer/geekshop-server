from django.shortcuts import render
# import json
# import os
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    data = {'title': 'GeekSHOP'}
    return render(request, 'products/index.html', context=data)


def products(request, category_id=None, page=1):
    data = dict()
    data['title'] = 'GeekPRODUCTS'
    data['category_list'] = ProductCategory.objects.all()
    # data['product_list'] = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    products_list = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products_list, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    data['product_list'] = products_paginator
    return render(request, 'products/products.html', context=data)


