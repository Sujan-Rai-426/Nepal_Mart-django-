


# Manually created file

from django.urls import path
from Cart import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('cart_products/', views.Cart_Products_View, name='cart_products'),
    path('add_cart/', views.Add_Cart_View, name='add_cart'),
    path('update_cart/', views.Update_Cart_View, name='update_cart'),
    path('delete_cart/', views.Delete_Cart_View, name='delete_cart'),

]