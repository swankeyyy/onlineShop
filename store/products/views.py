from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from users.models import User


# Create your views here.

def index(request):
    return render(request, 'products/index.html')


def products(request):
    content = Product.objects.all()
    context = {'items': content}
    return render(request, 'products/products.html', context=context)


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

