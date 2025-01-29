from uuid import uuid4

from django.conf import settings
from django.db import models

from ecommerce.store.models.product import Product


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders',
        null=True,
        blank=True,
    )
    order_item = models.ManyToManyField(
        Product, through='OrderItem', related_name='orders'
    )

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
