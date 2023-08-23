from django.contrib import admin
from .models import Collection, Product, Review, Customer, Cart, CartItem, Order, OrderItem

# Register your models here.


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    '''Admin View for Collection'''

    list_display = ('id', 'title')
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('id', 'title', 'description', 'slug',
                    'image', 'price', 'collection')

    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''Admin View for Review'''

    list_display = ('id', 'name', 'description', 'product', 'date', )
    list_per_page = 10


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Admin View for Cust'''

    list_display = ('id', 'first_name', 'last_name',
                    'phone', 'birth_date', 'user')
    list_per_page = 10


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''Admin View for Cart'''

    list_display = ('id', 'created_at')
    list_per_page = 10


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    '''Admin View for CartItem'''

    list_display = ('id', 'cart', 'product', 'quantity', )
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('id', 'placed_at',
                    'payment_status', 'customer', )
    list_editable = ['payment_status']
    list_per_page = 10


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''

    list_display = ('id', 'order', 'product', 'quantity', 'price', )
    list_per_page = 10
