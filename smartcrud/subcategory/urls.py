from django.urls import path
from .import views

urlpatterns = [
     path('', views.subcategory_index, name='subcategory_index'),
     path('create', views.subcategory_create, name='subcategory_create'),
     path('store', views.subcategory_store, name='subcategory_store'),
     path('delete/<int:pk>', views.subcategory_delete, name='subcategory_delete'),
     path('edit/<int:pk>', views.subcategory_edit, name='subcategory_edit'),
     path('update/<int:pk>', views.subcategory_update, name='subcategory_update'),
]