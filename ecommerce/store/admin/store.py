from django.contrib import admin

from ecommerce.store.models.store import Store


@admin.register(Store)
class Store(admin.ModelAdmin): ...
