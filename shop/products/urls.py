from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('', views.products_list, name='list'),
    path('<int:id>/', views.product_page, name='page'),
    

    path('products/', views.product_list2, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:id>/edit/', views.product_edit, name='product_edit'),
    path('<int:id>/delete/', views.product_delete, name='product_delete'),
    

    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),
]