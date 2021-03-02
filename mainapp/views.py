from django.shortcuts import render

import json
import os

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    products_file = os.path.join(os.getcwd(), 'mainapp', 'fixtures', 'products.json')
    context = {
        'title': 'geekshop - Каталог товаров',
        'products': json.load(open(products_file, encoding='utf-8')),
    }
    return render(request, 'mainapp/products.html', context)
