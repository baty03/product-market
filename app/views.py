from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Color

def index(request):

    products = Product.objects.all()

    return render(request, 'index.html', {
        'products': products
    })


# Create your views here.
