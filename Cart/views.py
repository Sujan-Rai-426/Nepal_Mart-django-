from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render


# Create your views here.
from django.contrib import messages
from Cart.cart import Cart
from Store.models import Product


# <----------> Logic to show Products in Cart <---------->
def Cart_Products_View(request):
    cart= Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantity
    totals = cart.cart_total_cost() # <-- object that contain value of  Calculate Total cost of Product in Cart
    return render(request, 'Cart/cart_products.html', {'cart_products':cart_products, 'quantities':quantities, 'totals':totals })


# <----------> Logic to Add Product in Cart <---------->
def Add_Cart_View(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__() # to update number or length of product in cart
        response = JsonResponse({'qty':cart_quantity})
        messages.success(request, 'Product added to the cart successfully..')
        return response



# <----------> Logic to Update Product in Cart <---------->
def Update_Cart_View(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        messages.info(request, 'Product cart has been updated successfully..')
        return response



# <----------> Logic to Delete Product in Cart <---------->
def Delete_Cart_View(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response = JsonResponse({'product':product_id})
        messages.info(request, 'Product cart has been deleted successfully..')
        return response



