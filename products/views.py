from django.shortcuts import render, get_object_or_404
from products import models


def main(request):
    products = models.Product.objects.all()
    products = products.filter(name__icontains='milk')
    return render(request, 'products/main_page.html', {'products': products})


def detail(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
