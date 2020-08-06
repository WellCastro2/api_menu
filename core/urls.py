from django.urls import path
from core import views

urlpatterns = [
    path('', views.root, name='api'),
    path('customer/', views.CustomerList.as_view(), name='customer-list'),
]