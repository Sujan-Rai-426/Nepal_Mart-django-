
# Manually created file

from django.urls import path
from Store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.Store_Index_View, name='store_index_user'),
    path('all_products/', views.All_Product_View, name='all_products'),
    
    
    path('search_product/', views.Search_Product_View, name='search_product'),
    
    path('coming_soon/', views.Coming_Soon_View, name='coming_soon'),
    
    path('product_detail/<int:pk>', views.Product_Detail_View, name = 'product_detail'), # product_detail path button is 'Buy Now'
    path('category/<str:suj>', views.Category_View, name='category'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)