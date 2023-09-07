# create_fake_date

import random

from django.core.management.base import BaseCommand
from home2.models import Client, Product, Order


class Command(BaseCommand):

    help = "Generate fake clients, products, orders."

    def _create_client(self, index: int):
        client = Client(name=f"client_{index}", email=f"client_{index}@email.com", tel="12345678901",
                        adress=f"address client_{index}" )
        client.save()

    def _create_product(self, index: int) -> None:
        product = Product(name=f"product_{index}", description=f"description product_{index}",
                          price=1.00, count=random.randint(0,10))
        product.save()

    def _create_orders(self, client_id: int, count_products: int):
        count_client_products = random.randint(1, count_products)
        for i in range(count_client_products):
            product_id = random.randint(1, count_products)
            product = Product.objects.filter(id=product_id).first()
            max_count_product = product.count
            if max_count_product:
                count = random.randint(1, max_count_product)
                order = Order(client_id = client_id,product_id = product_id,common_count=count)
                order.save()
                product.count = max_count_product - count
                product.save()


    def add_arguments(self, parser):
        parser.add_argument('count_clients', type=int, help='count clients')
        parser.add_argument('count_products', type=int, help='count products')

    def handle(self, *args, **kwargs):

        count_clients = kwargs.get('count_clients')
        count_products = kwargs.get('count_products')

        # заполнение таблицы товаров
        for j in range(count_products):
            self._create_product(j)

        # заполнение таблицы клиентов и заказов
        for i in range(count_clients):
            self._create_client(i)			            # заполнение таблицы клиентов

        for i in range(count_clients):
            self._create_orders(i+1, count_products)   	# заполение таблицы заказов


