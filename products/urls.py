from django.urls import path
from .views import ProductDetailView, ProductListView, ProductSearchListView

app_name= 'products' 


urlpatterns = [

     path('', ProductListView.as_view(), name='users_list'),
     path('search', ProductSearchListView.as_view(), name='search'),
     path('<slug:slug>', ProductDetailView.as_view(), name='Detail_product'),
   
]

