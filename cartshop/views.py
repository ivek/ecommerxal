from django.shortcuts import render
from .models import CartShop
from .utils import get_or_create_cart
# Create your views here.
def cart(request):
    

    cart = get_or_create_cart(request)

    return render(request, 'cartshop/cart.html',{
        
    })