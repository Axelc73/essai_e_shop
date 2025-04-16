from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from store.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/detail.html', context)
