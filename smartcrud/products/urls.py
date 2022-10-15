from django.urls import path
from .import views


urlpatterns = [
    path('', views.product_index, name='product_index'),
    path('create/', views.product_create, name='product_create'),
    path('store', views.product_store, name='product_store'),
    path('edit/<int:id>', views.product_edit, name='product_edit'),
    path('update/<int:id>', views.product_update, name='product_update'),
    path('view/<int:id>', views.product_view, name='product_view'),
    path('delete/<int:id>', views.product_delete, name='product_delete')
]


