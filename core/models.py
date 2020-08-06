from core.common.base import BaseModel
from django.db import models


class Customer(BaseModel):
    first_name = models.CharField("Primeiro Nome", max_length=50, blank=False, null=False)
    last_name = models.CharField("Último nome", max_length=50, blank=False, null=False)
    email = models.EmailField("E-mail", max_length=30)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.email


class Order(BaseModel):

    STATUS_CREATING = 1
    STATUS_PAID = 2
    STATUS_DELIVERED = 3
    STATUS_CANCEL = 4

    STATUS_OPTIONS = (
        (STATUS_CREATING, 'Criado'),
        (STATUS_PAID, 'Pago'),
        (STATUS_DELIVERED, 'Entregue'),
        (STATUS_CANCEL, 'Cancelado'),
    )

    status = models.IntegerField(choices=STATUS_OPTIONS, default=STATUS_CREATING)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField("Total", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.customer