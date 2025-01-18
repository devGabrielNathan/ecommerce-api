from uuid import uuid4

from django.db import models

from ecommerce.core.utils import Status


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.ACTIVE
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
