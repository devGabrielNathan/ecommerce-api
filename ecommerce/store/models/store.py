from uuid import uuid4

from django.db import models

from ecommerce.users.models.address import Address


class Store(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, related_name='store'
    )

    def __str__(self) -> str:
        return f'{self.name}'
