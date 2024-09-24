from django.contrib import admin
from .models import CartItem
#
#
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity')
    list_filter = ('customer', 'product')  # Filter by customer and product
    search_fields = ('customer__user__username', 'product__title')  # Search by customer username and product title
    ordering = ('customer',)
