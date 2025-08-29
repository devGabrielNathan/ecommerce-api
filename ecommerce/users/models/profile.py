from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(blank=True)
    avatar = CloudinaryField(
        'avatar',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
