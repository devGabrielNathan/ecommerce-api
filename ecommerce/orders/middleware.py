from django.utils.deprecation import MiddlewareMixin

from ecommerce.orders.models.order import Order


class StatelessOrderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        order_id = request.headers.get('X-Order-ID')

        if order_id:
            request.order, _ = Order.objects.get_or_create(
                id=order_id, user=None
            )
        else:
            request.order = None
