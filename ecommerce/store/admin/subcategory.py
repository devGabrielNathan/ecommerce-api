from django.contrib import admin

from ecommerce.store.models.subcategory import Subcategory


@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin): ...
