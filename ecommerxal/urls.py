
from django.contrib import admin
from django.urls import path, include

from users import urls




urlpatterns = [

    path('', include('users.urls')),
    path('productos/', include('products.urls')),
    path('admin/', admin.site.urls),
]
