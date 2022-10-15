
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product
from .forms import ProductForm
from account.models import Category, Subcategory
import os


# Create your views here.
def product_index(request):
     products = Product.objects.order_by('-id')
     paginator = Paginator(products, 2)
     page_number = request.GET.get('page')
     products = paginator.get_page(page_number)
     

     if 'title' in request.GET:
          title = request.GET['title']
          if title:
               products = Product.objects.filter(product_title__iexact=title)

     if 'varient' in request.GET:
          varient = request.GET['varient']
          if varient:
               products = Product.objects.filter(product_varient__iexact=varient)

     if 'min_price' in request.GET:
          min_price = request.GET['min_price']
          max_price = request.GET['max_price']
          if min_price:
               products = Product.objects.filter(product_price__range=[min_price, max_price])

     context = {
          'products' : products, 
     }
     return render(request, 'backend/product/index.html', context)


def product_create(request):
     
     categories = Category.objects.all()
     subcategories = Subcategory.objects.all()
     context = {
          'categories' : categories,
          'subcategories' : subcategories
      }
     return render(request, 'backend/product/create.html', context)


def product_store(request):
     if request.method == 'POST':
          data = request.POST
          image = request.FILES.get('product_image')
          Product.objects.create(
               product_title = data['product_title'],
               product_desc = data['product_desc'],
               product_price = data['product_price'],
               product_varient = data['product_varient'],
               in_stock = data['in_stock'],
               status = data['status'],
               product_slug = data['product_slug'],
               category_id = data['category_id'],
               subcategory_id = data['subcategory_id'],
               product_image = image,
          )
     
          messages.success(request, 'Product added success !')
          return redirect('product_index')

     return render(request, 'backend/product/create.html')



def product_edit(request , id):
     pid = Product.objects.get(id=id)
     categories = Category.objects.all()
     subcategories = Subcategory.objects.all()
     context = {
          'pid' : pid,
          'categories' : categories,
          'subcategories' : subcategories
     }
     return render(request, 'backend/product/edit.html', context)


def product_update(request, id):
     prod = Product.objects.get(id=id)

     if request.method == 'POST':
          if len(request.FILES) != 0:
               if len(prod.product_image) > 0:
                    os.remove(prod.product_image.path)
               prod.product_image = request.FILES['product_image']
          
          prod.product_title = request.POST.get('product_title')
          prod.product_desc = request.POST.get('product_desc')
          prod.product_price = request.POST.get('product_price')
          prod.product_varient = request.POST.get('product_varient')
          prod.in_stock = request.POST.get('in_stock')
          prod.status = request.POST.get('status')
          prod.product_slug = request.POST.get('product_slug')
          prod.category_id = request.POST.get('category_id')
          prod.subcategory_id = request.POST.get('subcategory_id')
          prod.save()
          messages.success(request, "Product update success")
          return redirect('product_index')


     return render(request, 'backend/product/edit.html')


def product_view(request, id):
     pid = Product.objects.get(id=id)
     context = {'pid' : pid}
     return render(request, 'backend/product/view.html', context)




def product_delete(request ,id):
     pid = Product.objects.get(id=id)
     if len(pid.product_image) > 0:
          os.remove(pid.product_image.path)
     pid.delete()
     messages.success(request, 'Product delete success')
     return redirect('product_index')
    