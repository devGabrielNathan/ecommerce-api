from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )
    password = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )


    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
