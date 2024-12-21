from uuid import uuid4

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractCommonInfo(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer.'
            + 'Letters, digits and @/./+/-/_ only.'
        ),
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    email = models.EmailField(_('email address'), max_length=150)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            + 'Unselect this instead of deleting accounts.'
        ),
    )

    class Meta:
        abstract = True
