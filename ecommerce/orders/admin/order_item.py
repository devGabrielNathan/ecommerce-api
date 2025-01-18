from django.contrib import admin

from ecommerce.orders.models.order_item import OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin): ...
