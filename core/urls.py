from django.urls import path
from core import views

urlpatterns = [
    path('clientes/', views.CustomerList.as_view(), name='customer-list'),
    path('clientes/<uuid:pk>', views.Customer.as_view(), name='customer'),

    path('pedidos/', views.OrderList.as_view(), name='order-list'),
    path('pedidos/<uuid:pk>', views.Order.as_view(), name='order'),
]