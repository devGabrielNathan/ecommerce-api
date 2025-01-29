from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenRefreshView


class RefreshToken(TokenRefreshView):
    @swagger_auto_schema(
        tags=['Users'],
        operation_summary='Atualizar Token JWT',
        operation_description='Recebe um refresh token válido e retorna um novo access token.',
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
