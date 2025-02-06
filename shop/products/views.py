from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def products_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()


    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(title__icontains=search_query)


    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)


    sort = request.GET.get('sort', 'title')
    if sort == 'price':
        products = products.order_by('price')
    elif sort == '-price':
        products = products.order_by('-price')
    else:
        products = products.order_by('title')

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query
    }
    
    return render(request, 'products/products_list.html', context)


def product_page(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_page.html', { 'product': product })

def homepage(request):
    new_arrivals = Product.objects.filter(available=True).order_by('-id')[:4]
    categories = Category.objects.all()[:3]
    
    return render(request, 'products/homepage.html', {
        'new_arrivals': new_arrivals,
        'categories': categories,
    })
    
@login_required
def product_list2(request):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    products = Product.objects.all()
    return render(request, 'products/product_list2.html', {'products': products})
    
@login_required
def product_create(request):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успішно створено')
            return redirect('products:list')
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Додати продукт'})

@login_required
def product_edit(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успішно оновлено')
            return redirect('products:list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', 
                 {'form': form, 'product': product, 'title': 'Редагувати продукт'})

@login_required
def product_delete(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успішно видалено')
        return redirect('products:list')
    
    return render(request, 'products/product_confirm_delete.html', {'product': product})

# Category Management Views
@login_required
def category_list(request):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категорію успішно створено')
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'products/category_form.html', {'form': form, 'title': 'Додати категорію'})

@login_required
def category_edit(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категорію успішно оновлено')
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'products/category_form.html', 
                 {'form': form, 'category': category, 'title': 'Редагувати категорію'})

@login_required
def category_delete(request, id):
    if not request.user.is_authenticated:
        messages.error(request, 'У вас немає доступу до цієї сторінки')
        return redirect('products:list')
        
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Категорію успішно видалено')
        return redirect('products:category_list')
    
    return render(request, 'products/category_confirm_delete.html', {'category': category})
    
    