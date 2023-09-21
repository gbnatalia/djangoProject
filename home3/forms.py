'''
a)Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
Создайте форму для редактирования товаров в базе данных.

б) Измените модель продукта, добавьте поле для хранения фотографии продукта.
Создайте форму, которая позволит сохранять фото.
'''
from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(label='Наименование', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название продукта'}))
    description = forms.CharField(label='Описание',max_length=1000,
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control', 'placeholder': 'Описание продукта'}))
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    count = forms.IntegerField(label='Колличество', min_value=0)
    image  = forms.ImageField(label='Изображение', required=False)

class ImageForm(forms.Form):
    image = forms.ImageField()
