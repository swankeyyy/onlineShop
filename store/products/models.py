from django.db import models
from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='%d/%m/%Y')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт {self.product.name}'