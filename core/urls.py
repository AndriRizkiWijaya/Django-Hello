from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('dashboard.urls')),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls'))
]
