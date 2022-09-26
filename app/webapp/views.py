from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


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
