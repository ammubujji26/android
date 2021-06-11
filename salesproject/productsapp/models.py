from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=90)
    product_category=models.CharField(max_length=40)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()
