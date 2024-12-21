# from uuid import uuid4

# from django.db import models
# from ecommerce.products.models import Product


# # Create your models here.
# class Order(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )
#     quantity = models.PositiveIntegerField(
#         default=1,
#     )


#     def __str__(self) -> str:
#         ...


#     class Meta:
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'


# class OrderItem(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )
#     order = models.ForeignKey(

#     )
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.PROTECT,
#     )


#     def __str__(self) -> str:
#         ...


#     class Meta:
#         verbose_name = 'OrderItem'
#         verbose_name_plural = 'OrderItems'


# class Payment(models.Model):
#     uuid = models.UUIDField(
#         primary_key=True,
#         unique=True,
#         default=uuid4,
#         editable=False
#     )


#     def __str__(self) -> str:
#         ...


#     class Meta:
#         verbose_name = 'Payment'
#         verbose_name_plural = 'Payments'
