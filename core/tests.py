from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Customer, Order
from rest_framework import status
from rest_framework.test import APITestCase


class BaseViewTest(APITestCase):

    URL_CUSTOMERS = reverse('customer-list')
    URL_ORDERS = reverse('order-list')

    def setUp(self):
        # create temp user
        self.name = 'TestUser'
        self.passw = 'Menu#123'
        self.user = User.objects.create_user(username=self.name, password=self.passw)

        # auth client api
        self.client.login(username=self.name, password=self.passw)

    def create_customer(self):
        data = {
            'first_name': 'Menu',
            'last_name': 'Non',
            'email': 'Qtest@anon.com'
        }

        return self.client.post(self.URL_CUSTOMERS, data)

    def create_order(self, total, customer):

        order = {
            'total': total,
            'customer': customer,
        }

        return self.client.post(self.URL_ORDERS, order)
    
    def update_order(self, status, uuid):
        URL_ORDER = reverse('order', args=(uuid,))
        data = {
            'status': 2,
            'total': 15.90
        }

        return self.client.put(URL_ORDER, data)
    
    def delete_order(self, uuid):
        URL_ORDER = reverse('order', args=(uuid,))

        return self.client.delete(URL_ORDER)


class TestIntegrationFull(BaseViewTest):

    def test_flow(self):
        """
        Full flow customer and order test
        """
        # CUSTOMER
        customer = self.create_customer()

        # check code created response
        self.assertEqual(status.HTTP_201_CREATED, customer.status_code)
        customer = customer.json()

        # ORDER
        order = self.create_order(199.90, customer.get('uuid'))
        # check code created response
        self.assertEqual(status.HTTP_201_CREATED, order.status_code)

        # ORDER update
        new_status = 2
        order_uuid = order.json().get('uuid')
        order_update = self.update_order(new_status, order_uuid)
        self.assertEqual(status.HTTP_200_OK, order_update.status_code)

        # check new status
        self.assertEqual(new_status, order_update.json().get('status'))

        # ORDER delete
        order_delete = self.delete_order(order_uuid)
        self.assertEqual(status.HTTP_204_NO_CONTENT, order_delete.status_code)
