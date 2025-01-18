from django.contrib import admin

from ecommerce.orders.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): ...
