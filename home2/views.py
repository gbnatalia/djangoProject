from django.http import HttpResponse
from home2.models import Client, Product, Order


def client(request):
    clients = Client.objects.all()
    data = ""
    for cl in clients:
        data += str(cl)+'<br>'
    return HttpResponse(data)

def product(request):
    products = Product.objects.all()
    data = ""
    for prod in products:
        data += str(prod)+'<br>'
    return HttpResponse(data)

def order(request):
    orders = Order.objects.all()
    data = ""
    for orde in orders:
        data += str(orde)+'<br>'
    return HttpResponse(data)
