from uuid import uuid4

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
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
    password = models.CharField('password', max_length=128)
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            + 'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            'Designates whether the user can log into this admin site.'
        ),
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f'{self.username} - {self.email}'
