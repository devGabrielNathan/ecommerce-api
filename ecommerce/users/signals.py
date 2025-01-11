from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate

User = get_user_model()


def create_default_admin_user(sender, **kwargs):
    email = 'admin@admin.com'
    username = 'admin'
    password = 'admin@admin123'

    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(
            email=email, username=username, password=password
        )


post_migrate.connect(create_default_admin_user)
