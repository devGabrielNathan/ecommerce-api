from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny

from ecommerce.users.models.profile import Profile
from ecommerce.users.serializers.profile import ProfileSerializer

swagger_attr = {'tags': ['Profiles']}

class ProfileGenericAPIView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_queryset(self):
        profile = Profile.objects.filter(user=self.request.user)
        return profile

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Recuperar perfil do usuário',
        operation_description='Recuperar perfil do usuário logado',
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        **swagger_attr,
        operation_summary='Atualizar perfil do usuário',
        operation_description='Atualizar perfil do usuário logado',
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

