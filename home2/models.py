from django.db import models

class Client(models.Model):
    '''
	Модель "Клиент":
		○ имя клиента
		○ электронная почта клиента
		○ номер телефона клиента
		○ адрес клиента
		○ дата регистрации клиента
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=11)
    adress = models.CharField(max_length=300)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.tel} {self.adress} {self.reg_date}'


class Product(models.Model):
    '''
	Модель "Товар":
		○ название товара
		○ описание товара
		○ цена товара
		○ количество товара
		○ дата добавления товара
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.count} {self.add_date}'


class Order(models.Model):
    '''
	Модель заказ:
		○ связь с моделью "Клиент", указывает на клиента,cделавшего заказ
		○ связь с моделью "Товар", указывает на товары, входящие в заказ
		○ общая сумма заказа
		○ дата оформления заказа
    '''
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    common_count = models.IntegerField(default=0)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.product} {self.common_count} {self.order_date}'