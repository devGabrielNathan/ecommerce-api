from uuid import uuid4

from django.db import models

from ecommerce.core.utils import Status
from ecommerce.store.models.subcategory import Subcategory
from ecommerce.users.models.supplier import Supplier


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, related_name='products'
    )
    product_supplier = models.ManyToManyField(
        Supplier, through='ProductSupplier', related_name='products'
    )

    def __str__(self) -> str:
        return f'{self.brand} - {self.name}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
