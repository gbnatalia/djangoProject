from django.contrib import admin
from .models import Client, Product, Order


#admin.site.register(Client)
#admin.site.register(Product)
#admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_help_text = 'Поиск по полю Описание продукта (description)'
    search_fields = ['description']
    list_display = ['name', 'description', 'price', 'count', 'image']
    readonly_fields = ['add_date']
    ordering = ['-count']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_help_text = 'Поиск по имени'
    search_fields = ['name']
    list_display = ['name', 'email', 'tel', 'adress', 'reg_date']
    ordering = ['name']
    readonly_fields = ['reg_date']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'total_price']
    readonly_fields = ['order_date']

