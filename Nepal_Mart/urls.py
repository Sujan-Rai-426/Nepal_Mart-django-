

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
    path('Store/', include('Store.urls')),
    path('Cart/', include('Cart.urls')),
    path('Account/', include('Account.urls')),
]
