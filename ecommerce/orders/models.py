from uuid import uuid4

from django.db import models


# Create your models here.
class Order(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )



    def __str__(self) -> str:
        ...


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )


    def __str__(self) -> str:
        ...


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
