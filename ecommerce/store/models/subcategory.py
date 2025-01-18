from uuid import uuid4

from django.db import models

from ecommerce.core.utils import Status
from ecommerce.store.models.category import Category


class Subcategory(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories'
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'subcategory'
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
