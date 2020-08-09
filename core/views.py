from rest_framework import generics

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer, OrderPostSerializer, OrderPutSerializer


class CustomerList(generics.ListCreateAPIView):
    """
    Retorna uma lista de todos os clientes.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Customer(generics.RetrieveUpdateDestroyAPIView):
    """
    Cliente por UUID.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderList(generics.ListCreateAPIView):
    """
    Retorna uma lista de todos os pedidos.
    """
    queryset = Order.objects.all()
    # serializer_class = OrderSerializer

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return OrderPostSerializer
        else:
            return OrderSerializer

    def perform_create(self, serializer):
        serializer.validate_items()
        serializer.save()


class Order(generics.RetrieveUpdateDestroyAPIView):
    """
    Pedido por UUID.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        action = self.request.method

        if action in ['PUT', 'PATCH']:
            return OrderPutSerializer
        elif action != 'GET':
            return OrderPostSerializer
        else:
            return OrderSerializer

    def perform_create(self, serializer):
        serializer.validate_items()
        serializer.save()
