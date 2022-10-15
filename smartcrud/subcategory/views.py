from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import SubcategoryForm
from account.models import Subcategory, Category
from django.contrib import messages




# Create your views here.
def subcategory_index(request):
     subcategories = Subcategory.objects.all().order_by('-id')
     if 'q' in request.GET:
          q = request.GET['q']
          page = Subcategory.objects.filter(subcategory_name__icontains=q)
          
     else:
          paginator = Paginator(subcategories, 3)
          page_number = request.GET.get('page')
          page = paginator.get_page(page_number)


     context = {'page' : page, 'subcategories' :subcategories }
     return render(request, 'backend/subcategory/index.html', context)


def subcategory_create(request):
     categories = Category.objects.all()
     context = {'categories' : categories}
     return render(request, 'backend/subcategory/create.html', context)



def subcategory_store(request):
     if request.method == 'POST':
          fm = SubcategoryForm(request.POST)
          if fm.is_valid():
               fm.save()
               return redirect('subcategory_index')
          else:
               print("something went worng ")
     else:
          fm = SubcategoryForm()
     context = {'fm' : fm}
     return render(request, 'backend/subcategory/create.html', context)



def subcategory_edit(request, pk):
     sub_cat_id = Subcategory.objects.get(id=pk)
     categories = Category.objects.all()
     context = {'sub_cat_id' : sub_cat_id, 'categories' : categories}
     return render(request, 'backend/subcategory/edit.html', context)


def subcategory_update(request, pk):
     if request.method == 'POST':
          sub_cat_id = Subcategory.objects.get(id=pk)
          fm = SubcategoryForm(request.POST, instance=sub_cat_id)
          if fm.is_valid():
               fm.save()
               messages.success(request, 'Subcategory update success')
               return redirect('subcategory_index')
          else:
               messages.error(request, 'Subcategory not updated')
               return redirect('subcategory_index')

     else:
          fm = SubcategoryForm()
     context = {'fm' : fm}
     return render(request, 'backend/subcategory/edit.html', context)


def subcategory_delete(request, pk):
     subcate_id = Subcategory.objects.get(id=pk)
     subcate_id.delete()
     return redirect('subcategory_index')




 