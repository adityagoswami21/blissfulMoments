from store.models import Product


class Cart():
    def __init__(self,request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        # Make sure cart is available on all the pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # Logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)


        self.session.modified = True

    def cart_total(self):
        # Get product ids
        product_ids = self.cart.keys()
        # lookup those keys in our product db model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0
        for key, value in quantities.items():
            # Convert key into string so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price*value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
 
    def update(self, product, quantity):
        # {'4':3, '2':5}
        product_id = str(product)
        product_qty = int(quantity)
        # Get cart
        ourcart = self.cart
        # Update dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart

        return thing
    
    def delete(self, product):
        # {'4':3, '2':5}
        product_id = str(product)
        # Delete from dict
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
