from django.shortcuts import render
from .models import Category, Product, Color

def index(request):
    products = Product.objects.all()

    return render(request, 'main/index.html', {
        'products': products
    })
