from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from common.views import CommonTitleMixin


# Create your views here.

class IndexView(CommonTitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store - index'


class ProductsListView(CommonTitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'items'
    title = 'Spisok'


@login_required
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


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
