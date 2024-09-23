# from django.contrib import admin

# # Register your models here.

# from django.contrib import admin
# from .models import Customer, Categories, Products, CartItem, Order, Coupon, Checkout, TrackShipment, Refund, Review


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone_number', 'city', 'postal_code')  # Fields displayed in the list view
#     list_filter = ('city',)  # Filter customers by city
#     search_fields = ('user__username', 'phone_number', 'city')  # Search by username, phone, and city
#     ordering = ('user',)  # Orders by username


# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     search_fields = ('name', 'slug')
#     ordering = ('name',)


# @admin.register(Products)
# class ProductsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'stock', 'category')
#     list_filter = ('category', 'price')  # Filter by category and price
#     search_fields = ('title', 'description')  # Search by title and description
#     ordering = ('title',)


# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'product', 'quantity')
#     list_filter = ('customer', 'product')  # Filter by customer and product
#     search_fields = ('customer__user__username', 'product__title')  # Search by customer username and product title
#     ordering = ('customer',)


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'total_price', 'status', 'created_at')
#     list_filter = ('status', 'created_at')  # Filter by status and creation date
#     search_fields = ('customer__user__username', 'status')  # Search by customer username and order status
#     ordering = ('-created_at',)  # Orders by latest orders first


# @admin.register(Coupon)
# class CouponAdmin(admin.ModelAdmin):
#     list_display = ('code', 'discount', 'active', 'expires_at')
#     list_filter = ('active', 'expires_at')  # Filter by active status and expiration date
#     search_fields = ('code',)  # Search by coupon code
#     ordering = ('expires_at',)


# @admin.register(Checkout)
# class CheckoutAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'order', 'payment_status', 'shipping_address')
#     list_filter = ('payment_status',)  # Filter by payment status
#     search_fields = ('customer__user__username', 'order__id')  # Search by customer username and order ID
#     ordering = ('customer',)


# @admin.register(TrackShipment)
# class TrackShipmentAdmin(admin.ModelAdmin):
#     list_display = ('order', 'tracking_number', 'carrier', 'status', 'estimated_delivery')
#     list_filter = ('carrier', 'status')  # Filter by carrier and status
#     search_fields = ('tracking_number', 'order__id')  # Search by tracking number and order ID
#     ordering = ('-estimated_delivery',)  # Orders by closest estimated delivery date


# @admin.register(Refund)
# class RefundAdmin(admin.ModelAdmin):
#     list_display = ('order', 'status', 'reason', 'created_at')
#     list_filter = ('status', 'created_at')  # Filter by refund status and creation date
#     search_fields = ('order__id', 'status', 'reason')  # Search by order ID, refund status, and reason
#     ordering = ('-created_at',)  # Orders by latest refunds first


# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'product', 'rating', 'created_at')
#     list_filter = ('rating', 'created_at')  # Filter by rating and creation date
#     search_fields = ('customer__user__username', 'product__title')  # Search by customer username and product title
#     ordering = ('-created_at',)  # Orders by latest reviews first
