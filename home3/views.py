import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Client, Product, Order
from .forms import ProductForm, ImageForm

def client(request):
    template_name = "home3\\list_items.html"
    clients = Client.objects.all()
    context = dict()
    context['title'] = "Клиенты"
    context['items'] = clients
    return render(request, template_name, context)


def product(request):
    template_name = "home3\\list_items.html"
    products = Product.objects.all()
    context = dict()
    context['title'] = "Товары"
    context['items'] = products
    return render(request, template_name, context)


def order(request):
    template_name = "home3\\list_items.html"
    orders = Order.objects.all()
    context = dict()
    context['title'] = "Заказы"
    context['items'] = orders
    return render(request, template_name, context)


class OrderProductView(TemplateView):
    template_name = 'home3\\order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrderProductView, self).get_context_data(**kwargs)
        client = Client.objects.get(id=self.kwargs['pk'])
        orders = Order.objects.filter(client=client).all()
        context['client'] = client
        context['orders'] = orders
        context['title'] = "Список заказов клиента"
        return context


class ListClientProducts(TemplateView):
    template_name = 'home3\\products_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListClientProducts, self).get_context_data(**kwargs)
        enddate = datetime.date.today()
        startdate = enddate - datetime.timedelta(days=self.kwargs['days'])
        client = Client.objects.get(id=self.kwargs['pk'])
        orders = Order.objects.filter(client=client).filter(order_date__range=[startdate, enddate]).all().order_by('order_date')
        context['client'] = client
        context['orders'] = orders
        context['title'] = "Список заказов клиента"
        return context


def change_product(request, pk):

    product = Product.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            if isinstance(image, bool):
                image = None
            if image is not None:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.count = form.cleaned_data['count']
            product.image = image
            product.save()
    else:
        form = ProductForm(initial={'name': product.name, 'description': product.description,
                                    'price': product.price, 'count': product.count, 'image': product.image})

    return render(request, 'home3/change_product.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'home3/upload_image.html', {'form': form})


