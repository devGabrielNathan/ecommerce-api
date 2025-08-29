from django.contrib.auth import get_user_model
from rest_framework import serializers
from ecommerce.users.models.profile import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=True
    )

    class Meta:
        model = Profile
        fields = [
            'user',
            'bio',
            'avatar'
        ]
        read_only_fields = ['id', 'user']
