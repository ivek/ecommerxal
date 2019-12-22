from django.contrib import admin
from .models import Category

class CategoriesAdmin(admin.ModelAdmin):
    fields= ('title', 'description', 'products')
    list_display = ('__str__', 'created_at')
# Register your models here.
admin.site.register(Category, CategoriesAdmin)