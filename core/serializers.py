
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


class OrderPostSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(write_only=True)
    class Meta:

        model = Order
        fields = ('uuid','status', 'total', 'customer', 'created_at')

    def validate_items(self):
        customer_uuid = self.validated_data.get('customer')
        # check DB user exists
        if not Customer.objects.filter(uuid=customer_uuid).exists():
            raise serializers.ValidationError('Customer not found')

    def create(self, validated_data):
        validated_data['customer'] = Customer.objects.get(uuid=validated_data['customer'])
        return super(OrderPostSerializer, self).create(validated_data)


class OrderPutSerializer(serializers.ModelSerializer):
    class Meta:

        model = Order
        fields = ('uuid','status', 'total')