from django.contrib import admin

from ecommerce.store.models.product import Product


@admin.register(Product)
class Product(admin.ModelAdmin): ...
