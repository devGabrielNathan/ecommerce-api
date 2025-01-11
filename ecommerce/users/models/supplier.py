from uuid import uuid4

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


# Create your models here.
class Supplier(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text=(
            'Required. 150 characters or fewer.'
            + 'Letters, digits and @/./+/-/_ only.'
        ),
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': ('A user with that username already exists.'),
        },
    )
    email = models.EmailField('email address', unique=True, max_length=150)
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            + 'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        db_table = 'supplier'
        verbose_name = 'supplier'
        verbose_name_plural = 'suppliers'

    def __str__(self):
        return f'{self.username} - {self.email}'
