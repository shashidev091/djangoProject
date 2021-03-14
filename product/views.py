from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    # return HttpResponse('This is my first Api')
    return render(request, 'index.html', {'products': products})


def new_page(request):
    # return HttpResponse('This is new page create with /new Api')
    return JsonResponse({'message': 'yahoo'})
