from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('account.urls')),
    path('', include('user_auth.urls')), 
    path('subcategory/', include('subcategory.urls')),
    path('product/', include('products.urls'))


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)