from django.shortcuts import render, redirect
from .models import Product, Tag
from .forms import ProductForm

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    tags = product.tags.all()
    context = {'product': product, 'tags': tags}
    return render(request, 'products/product.html', context)

def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}

    return render(request, 'products/product_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form, 'product': product}
    return render(request, 'products/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')

    context = {'product': product}
    return render(request, 'products/delete_product.html', context)
