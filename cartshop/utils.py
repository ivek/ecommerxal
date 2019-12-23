from .models import CartShop

def get_or_create_cart(request):
        user = request.user if request.user.is_authenticated else None
        cart_id = request.session.get('cart_id')
        cart = CartShop.objects.filter(cart_id=cart_id).first()
        if cart is None:
            cart = CartShop.objects.create(user=user)    

        if user and cart.user is None:
            cart.user = user
            cart.save()

        request.session['cart_id']=cart.cart_id

        return cart