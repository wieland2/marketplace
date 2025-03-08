from django.shortcuts import render

def products(request):
    context = {}
    return render(request, 'products/products.html', context)


def product(request, pk):
    context = {'pk': pk}
    return render(request, 'products/product.html', context)
