from uuid import uuid4

from django.db import models

from ecommerce.orders.models.order import Order
from ecommerce.store.models import Product


# Create your models here.
class OrderItem(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order_items'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_items'
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.product.name} ({self.quantity})'

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    @property
    def get_total(self) -> float:
        return self.product.price * self.quantity
