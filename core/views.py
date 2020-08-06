from rest_framework import generics
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Customer
from .serializers import CustomerSerializer


@api_view()
def root(request):
        return Response({
            'customers': reverse('customer-list', request=request),
        })


class CustomerList(generics.ListCreateAPIView):
    """
    Retorna uma lista de todos os usuários do sistema.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer