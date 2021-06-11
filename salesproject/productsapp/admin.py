from django.contrib import admin
from productsapp.models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=['product_name','product_category','product_quantity','product_price']
admin.site.register(Products,ProductsAdmin)
