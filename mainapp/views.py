from django.shortcuts import render

import os
from mainapp.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'geekshop',
    }
    return render(request, 'mainapp/index.html', context)

def products(request, id=None):
    context = {
        'title': 'geekshop - Каталог товаров',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
