

#Manualy created file for session creation , this page help the cart session to work on all the pages
from .cart import Cart


def cart(request):
    return {'cart':Cart(request)}