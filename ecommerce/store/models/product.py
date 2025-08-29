from uuid import uuid4

from django.db import models

from ecommerce.core.utils import Status
from ecommerce.store.models.subcategory import Subcategory
# from cloudinary.models import CloudinaryField


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True, default='products/sacola_amarela.png')
    # image = CloudinaryField('image')
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, related_name='products'
    )

    def __str__(self) -> str:
        return f'{self.brand} - {self.name}'

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.status = Status.INACTIVE
        if self.quantity > 0 and self.status == Status.INACTIVE:
            self.status = Status.ACTIVE
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
