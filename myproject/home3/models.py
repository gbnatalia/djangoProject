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
    email = models.EmailField(default='email@mail.com')
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
    description = models.TextField(default='', blank=True, max_length=1000)
    price = models.DecimalField(default='0.00', max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    add_date = models.DateField(auto_now_add=True)
    image = models.ImageField(default="", null=True)

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.product} {self.total_price} {self.order_date}'
