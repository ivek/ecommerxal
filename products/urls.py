from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [

     path('', ProductListView.as_view(), name='users_list'),
     path('<slug:slug>', ProductDetailView.as_view(), name='Detail_product'),
   
]

