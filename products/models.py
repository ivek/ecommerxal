from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone
import uuid
# Create your models here
class Product(models.Model):
    title= models.CharField(max_length=50)
    description= models.TextField()
    image = models.ImageField(upload_to="products/", null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    create_at= models.DateTimeField(auto_now=True)

    #def save(self, *args, **kwargs):
     #   self.slug= slugify(self.title)
      #  super(Product,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
def set_slug(sender,instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)
    
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
               '{}-{}'.format(instance.title, str(uuid.uuid4())[:2]
               )
            )
        instance.slug = slug

pre_save.connect(set_slug, sender=Product)