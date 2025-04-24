from django.shortcuts import render, get_list_or_404, redirect
from .models import AllProducts
from django.http import HttpResponse
from .forms import AllProductsForm


# Create your views here.

def allProducts(request):
    allproducts = AllProducts.objects.all()
    context = {
        'title': 'Shop',
        'allproducts': allproducts,
    }
    template = 'app_shop/shop.html'
    return render(request, template, context)


def custom_dashboard_admin(request):
    product = AllProducts.objects.all().order_by('-id')
    context = {
        'title':'Dashboard',
        'product': product,
    }
    template = 'app_shop/custom_dashboard_admin.html'
    return render(request, template, context)


def edit_product(request, id):
    product = get_list_or_404(AllProducts, id=id)
    if product.method =='POST':
        form = AllProductsForm(request.POST, request.FILES, instance=(product))
        if form.is_valid():
            form.save()
            return redirect('admin_product')
    else:
        form = AllProductsForm(instance=product)
    context = {
        'title':'Edit Product',
        'form':form,
    }
    template = 'app_shop/edit_product.html'
    return render(request, template, context)

def add_product(request):
    product = AllProductsForm(request.POST or None, request.FILES or None)
    if product.is_valid():
        product.save()
        return redirect('dashboard_admin')
    else:
        product = AllProductsForm()
    context = {
        'title': 'Add Products',
        'form':product,
    }
    template = 'app_shop/add_product.html'
    return render(request, template, context)