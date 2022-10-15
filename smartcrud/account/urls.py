from django.urls import  path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('create/', views.categroy_create, name='categroy_create'),
    path('store/', views.category_store, name='category_store'),
    path('edit/<int:id>', views.category_edit, name='category_edit'),
    path('update/<int:id>', views.category_update, name='category_update'),
    path('delete/', views.category_delete, name='category_delete'),
]
