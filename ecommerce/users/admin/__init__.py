from ecommerce.users.admin.address import AddressAdmin, AddressInline
from ecommerce.users.admin.phone import PhoneAdmin, PhoneInline
from ecommerce.users.admin.supplier import SupplierAdmin
from ecommerce.users.admin.user import UserAdmin

__all__ = [
    'UserAdmin',
    'SupplierAdmin',
    'AddressAdmin',
    'AddressInline',
    'PhoneAdmin',
    'PhoneInline',
]
