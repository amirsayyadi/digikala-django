from shop.models import Product, Profile

class Cart():


    def __init__(self, request):
        self.session = request.session
        self.request = request

        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        if self.request.user.is_authenticated:
            user_profile = Profile.objects.filter(user__id= self.request.user.id)
            old_cart = str(self.cart).replace('\'', '\"')

            user_profile.update(old_cart= old_cart)
    

    def __len__(self):
        return len(self.cart)
    

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return products
    

    def get_quants(self):
        quantities = self.cart

        return quantities
    
    def get_total(self):

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)

        total = 0
        for key, value in self.cart.items():
            
            for product in products:
                if int(key) == product.id:

                    if product.is_sale:
                        total = total + int(value) * product.sale_price

                    else:
                        total = total + int(value) * product.price

        return total



    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        ourcart = self.cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        if self.request.user.is_authenticated:
            user_profile = Profile.objects.filter(user__id= self.request.user.id)
            old_cart = str(self.cart).replace('\'', '\"')

            user_profile.update(old_cart= old_cart)

        return self.cart


    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            user_profile = Profile.objects.filter(user__id= self.request.user.id)
            old_cart = str(self.cart).replace('\'', '\"')

            user_profile.update(old_cart= old_cart)
        return 
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True
