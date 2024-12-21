from rest_framework import status, viewsets
from rest_framework.response import Response

from ecommerce.core.models import Address, Phone
from ecommerce.core.serializers import AddressSerializer, PhoneSerializer


# Create your views here.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def create(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
