from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ecommerce.users.abstract_models import AbstractCommonInfo


# Create your models here.
# fmt: off
class User(AbstractCommonInfo, AbstractBaseUser, PermissionsMixin):
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractCommonInfo.Meta):
        db_table = 'user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return f'{self.username} - {self.email}'


class Supplier(AbstractCommonInfo):
    class Meta(AbstractCommonInfo.Meta):
        db_table = 'supplier'
        verbose_name = _('supplier')
        verbose_name_plural = _('suppliers')

    def __str__(self):
        return f'{self.username} - {self.email}'
# fmt: on
