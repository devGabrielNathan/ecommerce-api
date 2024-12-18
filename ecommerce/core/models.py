from uuid import uuid4

from django.db import models

from ecommerce.users.models import Supplier, User


# Create your models here.
class Address(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    state = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )
    city = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    neighborhood = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    street = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    complement = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    cep = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self) -> str:
        if not self.complement:
            address = f"{self.street} - {self.neighborhood}, {self.city} - {self.state}, {self.cep}"

        else:
            address = f"{self.street}, {self.number}, {self.complement},
            {self.neighborhood}, {self.city} - {self.state}, {self.cep}"

        return address


class Phone(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    DDD = models.CharField(
        max_length=3,
        default='21',
        null=False,
        blank=False
    )
    number = models.CharField(
        max_length=9,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='phones'
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='phones'
    )

    class Meta:
        db_table = 'phone'
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self) -> str:
        if self.DDD.startswith('0'):
            self.DDD = self.DDD[1:]

        return f"{self.DDD} {self.number}"
