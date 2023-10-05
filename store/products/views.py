from django.shortcuts import render
from .models import Product


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    content = Product.objects.all()
    context = {'items': content}
    return render(request, 'products/products.html', context=context)
