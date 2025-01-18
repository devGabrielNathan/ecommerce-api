from celery import shared_task
from django.utils import timezone


@shared_task
def update_product_quantity(product_supplier_id):
    try:
        from ecommerce.store.models.product_supplier import ProductSupplier
        product_supplier = ProductSupplier.objects.get(id=product_supplier_id)
        if timezone.now() >= product_supplier.delivery_date:
            product_supplier.product.quantity += product_supplier.quantity
            product_supplier.product.save()
    except ProductSupplier.DoesNotExist:
        pass
