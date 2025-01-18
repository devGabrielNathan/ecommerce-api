from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

from ecommerce.users.models.address import Address
from ecommerce.users.models.phone import Phone
from ecommerce.users.models.supplier import Supplier

User = get_user_model()


class Command(BaseCommand):
    help = 'Loads the necessary fixtures for the application.'

    def handle(self, *args, **kwargs):
        USERS_IN_DATABASE = 1

        if User.objects.count() <= USERS_IN_DATABASE:
            self.stdout.write(
                f'Users in database ({User.objects.count()}) is less than or equal to {USERS_IN_DATABASE}.'
            )

            dict_queryset = {
                'User': User.objects.exists(),
                'Supplier': Supplier.objects.exists(),
                'Phone': Phone.objects.exists(),
                'Address': Address.objects.exists(),
            }

            self.stdout.write(f'Model data existence: {dict_queryset}')

            if not all(dict_queryset.values()):
                try:
                    call_command('loaddata', 'users.json')
                    call_command('loaddata', 'suppliers.json')
                    call_command('loaddata', 'phones.json')
                    call_command('loaddata', 'store.json')
                    call_command('loaddata', 'addresses.json')
                    call_command('loaddata', 'orders.json')
                    call_command('loaddata', 'categories.json')
                    call_command('loaddata', 'subcategories.json')
                    call_command('loaddata', 'products.json')
                    # Ate aqui tudo bem
                    call_command('loaddata', 'order_items.json')
                    call_command('loaddata', 'product_supplier.json')
                    self.stdout.write(
                        self.style.SUCCESS('Fixtures loaded successfully!')
                    )
                except Exception as e:
                    self.stderr.write(f'Error loading fixtures: {e}')
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        'Database is not empty. No fixtures loaded.'
                    )
                )
        else:
            self.stdout.write(
                f'Users in database ({User.objects.count()}) is not less than {USERS_IN_DATABASE}. No fixtures loaded.'
            )
