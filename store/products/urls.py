from django.contrib import admin
from django.urls import path
from products.views import *

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:id>/', basket_remove, name='basket_remove')
]

