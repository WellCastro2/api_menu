from rest_framework import generics

from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer


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
    serializer_class = OrderSerializer


class Order(generics.RetrieveUpdateDestroyAPIView):
    """
    Pedido por UUID.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
