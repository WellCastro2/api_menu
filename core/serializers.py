
from rest_framework import serializers
from .models import Order
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = ('uuid', 'active', 'first_name', 'last_name', 'email')


class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()
    class Meta:

        model = Order
        fields = ('uuid','status', 'total', 'customer', 'created_at')
