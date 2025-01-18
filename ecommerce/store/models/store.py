from uuid import uuid4

from django.db import models


class Store(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'
