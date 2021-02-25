from django.contrib import admin
from accounts.models import Customer, Tag, Product, Order
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'phone', 'email', 'date_created']

admin.site.register(Customer, CustomerAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

admin.site.register(Tag, TagAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'price', 'category', 'discription', 'date_created']

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'customer', 'product', 'date_created', 'status']

admin.site.register(Order, OrderAdmin)
