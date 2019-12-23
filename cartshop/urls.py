from django.urls import path
from . import  views

app_name= 'cartshop' 


urlpatterns = [

     path('', views.cart, name='cart'),
     
   
]