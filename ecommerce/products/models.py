# from email.headerregistry import Address
# from uuid import uuid4

# from django.db import models

# from ecommerce.core.models import Phone


# class Category(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )
#     name = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False
#     )
#     status = models.BooleanField()

#     def __str__(self) -> str:
#         return f"{self.name}"

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'


# class Subcategory(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )
#     name = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False
#     )
#     status = models.BooleanField()

#     def __str__(self) -> str:
#         f"{self.name}"

#     class Meta:
#         verbose_name = 'Subcategory'
#         verbose_name_plural = 'Subcategories'


# # Create your models here.
# class Product(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )
#     name = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False
#     )
#     status = models.BooleanField()
#     description = models.TextField(
#         null=False,
#         blank=False
#     )
#     brand = models.CharField(
#         max_length=255,
#         null=False,
#         blank=False
#     )
#     price = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#         null=False,
#         blank=False
#     )
#     # image = models.ImageField(
#     # )
#     subcategories = models.ForeignKey(
#         Subcategory,
#         on_delete=models.PROTECT,
#         null=False,
#         blank=False
#     )

#     def __str__(self) -> str:
#         ...

#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'


# class ProductSupplier:
#     quantity = models.PositiveBigIntegerField(
#         default=1
#     )
#     destination = models.ForeignKey(
#         Address,
#         on_delete=models.PROTECT,
#         null=False,
#         blank=False
#     )
#     # delivery_date =
#     product = models.ForeignKey(
#         Product,
#         models.PROTECT,
#         null=False,
#         blank=False
#     )
#     supplier = models.ForeignKey(
#         Supplier,
#         on_delete=models.PROTECT,
#         null=False,
#         blank=False
#     )
