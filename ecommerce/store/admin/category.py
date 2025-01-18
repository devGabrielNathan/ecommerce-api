from django.contrib import admin

from ecommerce.store.models.category import Category


@admin.register(Category)
class Category(admin.ModelAdmin): ...
