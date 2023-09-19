from django.contrib import admin
from django.urls import path
from .views import OrderProductView, ListClientProducts
from .views import client, product, order, upload_image, change_product

urlpatterns = [
    path('client/', client, name='client'),
    path('product/', product, name='product'),
    path('order/', order, name='order'),
    path('orders/<int:pk>', OrderProductView.as_view(), name='OrderProductView'),
    path('products/<int:pk>/<int:days>', ListClientProducts.as_view(), name='ListClientProducts'),
    path('products/mod/<int:pk>', change_product, name='change_product'),
    path('upload/', upload_image, name='upload_image'),
]