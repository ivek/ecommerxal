import uuid
from django.db import models
from clients.models import User
from products.models import Product
from django.db.models.signals import pre_save


# Create your models here.
class CartShop(models.Model):
    cart_id= models.CharField(max_length=100, null=False, blank=False, unique=True)
    user= models.ForeignKey(User, null=True, blank= True, on_delete="models.CASCADE")
    product = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2) 
    create_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cart_id

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id= str(uuid.uuid4())

pre_save.connect(set_cart_id, sender=CartShop)
