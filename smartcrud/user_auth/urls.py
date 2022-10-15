from django.urls import path
from .import views


urlpatterns = [
    path('', views.frontend_index, name='frontend_index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.registration, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
]
