from django.shortcuts import render

import json
import os

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    file = os.path.join(os.getcwd(), 'mainapp', 'fixtures', 'products.json')
    with open(file, encoding='utf-8') as f:
        products_list = json.load(f)
    context = {
        'title': 'geekshop - Каталог товаров',
        'products': products_list,
    }
    return render(request, 'mainapp/products.html', context)
