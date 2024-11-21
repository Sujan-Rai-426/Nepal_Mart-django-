

# Created File manually and this file contains ....'FUNCTIONS'.... that will be used or call in views


# Main class Cart 
from Store.models import Product


class Cart():
        
            # <-----------------> Function to create SESSION ID <-------------------->
        def __init__(self, request):
            self.session = request.session
            cart = self.session.get('session_key')
            if 'session_key' not in request.session:
                cart = self.session['session_key']={}
            
            self.cart = cart
        
        
            # <--------------> Function that update length or number of product item in cart<----------------->
        def __len__(self):
            return len(self.cart)
        
        
        
            # <--------------> Function that can add product in cart<----------------->
        def add(self, product, quantity):
            product_id = str(product.id)
            product_qty = str(quantity)
            if product_id in self.cart:
                pass
            else:
                # self.cart[product_id] = {'price': str(product.price)}
                self.cart[product_id] = int(product_qty)
            self.session.modified=True
        
        
        
        # <--------------> Function that can get product in cart to display<----------------->
        def get_products(self):
            product_ids = self.cart.keys()
            products =Product.objects.filter(id__in=product_ids)
            return products
        
        
        
        # <--------------> Function that can get product quantity in cart to display<----------------->
        def get_quantity(self):
            quantities = self.cart
            return quantities
        
        
        
        # <--------------> Function that can update product in cart<----------------->
        def update(self, product, quantity):
            product_id = str(product)
            product_qty = int(quantity)
            ourcart = self.cart
            ourcart[product_id] = product_qty
            self.session.modified = True
            thing =self.cart
            return thing
        
        
        
        # <--------------> Function that can delete product from cart<----------------->
        def delete(self, product):
            product_id = str(product)
            if product_id in self.cart:
                del self.cart[product_id]
            self.session.modified = True
        
        
        
        # <--------------> Function that can calculate total cost of products in cart<----------------->
        def cart_total_cost(self):
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            quantities = self.cart
            total = 0
            for key,value in quantities.items():
                key = int(key)
                for product in products:
                    if product.id == key:
                        if product.in_sale:
                            total = total + (product.in_sale_price * value)
                        else:
                            total = total + (product.price * value)
            return total