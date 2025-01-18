from datetime import datetime, timedelta

from django.db import models

from ecommerce.store.models.product import Product
from ecommerce.store.models.store import Store
from ecommerce.users.models.supplier import Supplier


class ProductSupplier(models.Model):
    quantity = models.PositiveBigIntegerField(default=1)
    destination = models.ForeignKey(
        Store, models.PROTECT, related_name='product_suppliers'
    )
    delivery_date = models.DateTimeField(
        default=datetime.now() + timedelta(days=10)
    )
    product = models.ForeignKey(
        Product, models.PROTECT, null=False, blank=False
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, null=False, blank=False
    )

    def __str__(self) -> str:
        return f'{self.product.name} ({self.quantity})'

    def save(self, *args, **kwargs):
        self.product.quantity += self.quantity

        return super().save(*args, **kwargs)
