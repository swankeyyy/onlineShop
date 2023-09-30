from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='%d/%m/%Y')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    