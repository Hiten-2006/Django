from django.shortcuts import render
from .models import Customer, Product

def home(request):
    return render(request, 'home.html')

def add(request):
    try:
        val1 = int(request.POST.get('num1', 0) or 0)
        val2 = int(request.POST.get('num2', 0) or 0)
        val3 = val1 + val2
        return render(request, 'result.html', {'result': val3})
    except ValueError:
        return render(request, 'result.html', {'result': 'Invalid input'})

def dashboard(request): 
    customers = Customer.objects.all() 
    return render(request, 'dashboard.html', {'customers': customers})

def products(request): 
    products = Product.objects.all() 
    return render(request, 'product.html', {'products': products})
