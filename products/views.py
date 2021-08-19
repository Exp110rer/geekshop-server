from django.shortcuts import render
import json
import os


# Create your views here.

def index(request):
    data = {'title': 'GeekSHOP'}
    return render(request, 'products/index.html', context=data)


def products(request):
    data = {'title': 'GeekPRODUCTS'}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'products.json'), 'r') as file_obj:
        data['product_list'] = json.load(file_obj)
    return render(request, 'products/products.html', context=data)
