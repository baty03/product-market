from django.shortcuts import render
from .models import Category, Product, Color

def index(request):

    return render(request, 'main/index.html')


# Create your views here.
