from django.contrib import admin

from ecommerce.store.models.product_supplier import ProductSupplier


@admin.register(ProductSupplier)
class ProductSupplier(admin.ModelAdmin): ...
