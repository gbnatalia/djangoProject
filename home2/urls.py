from django.contrib import admin
from django.urls import path
from .views import client, product, order

urlpatterns = [
    path('client/', client, name='client'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
]
