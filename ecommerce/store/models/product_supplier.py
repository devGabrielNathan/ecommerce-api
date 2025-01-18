from datetime import datetime, timedelta
from uuid import uuid4

from django.db import models

from ecommerce.core.tasks import update_product_quantity
from ecommerce.store.models.product import Product
from ecommerce.store.models.store import Store
from ecommerce.users.models.supplier import Supplier


class ProductSupplier(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4,
        editable=False
    )
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
        super().save(*args, **kwargs)
        update_product_quantity.apply_async((self.id,), eta=self.delivery_date)

    @property
    def store_address(self):
        return self.destination.address
