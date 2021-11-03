from django.shortcuts import render
from .models import Product

# Create your views here.


def main(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'main.html', context)
