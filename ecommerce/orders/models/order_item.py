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
    subtotal = models.DecimalField(
        max_digits=8, decimal_places=2, editable=False, blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.product.name} ({self.quantity} - R$ {self.subtotal})'

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
        ordering = ['product__name']
