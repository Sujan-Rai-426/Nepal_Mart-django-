
# Create your views here.

from django.shortcuts import redirect, render
from Store.models import Category, Product
from django.contrib import messages
from django.db.models import Q


#  Just logic Page to Show Coming Soon html 
def Coming_Soon_View(request):
    return render(request,'Store/coming_soon.html')



# Logic to show Home page of store
def Store_Index_View(request):
    # Get all the Product in object
    products = Product.objects.all()
    return render(request, 'Store/index.html', {'products':products})



# Logic to show page for All products
def All_Product_View(request):
    # Get all the Product in object
    products = Product.objects.all()
    return render(request, 'Store/all_products.html', {'products':products})



# Logic to show the detail of each product when click 'Buy Now' button
def Product_Detail_View(request, pk):
    # Get id the Product in object to view specific product only which we click view detail
    products = Product.objects.all()
    product = Product.objects.get(id=pk)
    return render(request, 'Store/product_detail.html', {'product':product, 'products':products})



# Logic to show the Products in page when we choose category
def Category_View(request, suj):
    suj = suj.replace('-','')
    try:
        category = Category.objects.get(type=suj)
        products = Product.objects.filter(category=category)
        return render(request, 'Store/category.html', {'products':products, 'category':category})
    except:
        messages.success(request, ("That Category didn't exist..."))
        return redirect('store_index_user')



# Logic to show the products when we search in search bar
def Search_Product_View(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains=searched) |Q(description__icontains=searched) | Q(price__icontains=searched) | Q(in_sale__icontains=searched) | Q(in_sale_price__icontains=searched))
        if not searched:
            messages.error(request, 'Your searched product is not available right now...')
            return render(request, 'Store/search_product.html', {'searched':searched })
        else:
            return render(request, 'Store/search_product.html', {'searched':searched})
    else:
        return render(request, 'Store/index.html',{})



