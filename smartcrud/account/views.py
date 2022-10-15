from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
from django.contrib import messages 
from .models import Category
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='login')
def index(request):
    context = {'title' : 'Dashboard'}
    return render(request, 'backend/index.html', context)


@login_required(login_url='login')
def category(request):
    categorys = Category.objects.all().order_by('-id')
    paginator = Paginator(categorys, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context= {'page' : page, 'total' : categorys}
    return render(request, 'backend/category/index.html', context)


@login_required(login_url='login')
def categroy_create(request):
    return render(request, 'backend/category/create.html')



@login_required(login_url='login')
def category_store(request):
    if request.method == 'POST':
        fm = CategoryForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Category Added Success")
            return redirect('category')
       
    else: 
        fm = CategoryForm()
    context = {'fm' : fm}
    return render(request, 'backend/category/create.html', context)

    

@login_required(login_url='login')
def category_edit(request, id):
    cat_id = Category.objects.get(id=id)
    context = {'cat_id': cat_id}
    return render(request, 'backend/category/edit.html', context)


@login_required(login_url='login')
def category_update(request, id):
    if request.method == 'POST':
        cat_id = Category.objects.get(id=id)
        fm = CategoryForm(request.POST, instance=cat_id)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Category Update Success')
            return redirect('category')
    
    else:
        fm = CategoryForm()
    context = {'fm' : fm}
    return render(request, 'backend/category/edit.html')

@login_required(login_url='login')
@csrf_exempt
def category_delete(request):
    if request.method == 'POST':
        cat_id = request.POST.get('sid')
        pid = Category.objects.get(pk=cat_id)
        pid.delete()
        return JsonResponse({ 'status' : 1})
    else:
        return JsonResponse({'status' : 0})
    


