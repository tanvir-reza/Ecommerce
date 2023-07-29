class Cart():

    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart


    def add(self,product,qnt):
        product_id = str(product.id)

        if product.id in self.cart:
            self.cart[product_id][qnt] = qnt
        else:
            self.cart[product_id] = {'price':str(product.id),'qnt':str(qnt)}

        self.session.modified = True