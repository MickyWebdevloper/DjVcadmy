from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id','title', 'author', 'slug', 'price','in_stock','created','updated']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['in_stock', 'is_active']
    list_editable = ['in_stock','price']


