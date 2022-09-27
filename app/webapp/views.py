from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)


def single_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Category.objects.create(name=name, description=description)
        return redirect('/')


def product_add_view(request, *args, **kwargs):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, "product_add.html", context)
    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = Category.objects.get(pk=request.POST.get("category"))
        image = request.POST.get("image")
        product = Product.objects.create(name=name, description=description, price=price, category=category, image=image)
        url = reverse("product_view", kwargs={'pk': product.pk})
        return HttpResponseRedirect(url)


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)


def delete_category_view(request, category_id):
    categories = Category.objects.get(pk=category_id)
    categories.delete()
    return redirect('categories/')
