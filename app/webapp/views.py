from django.shortcuts import render

from webapp.models import Product


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return  render(request, 'products.html', context)
