from django.contrib import admin
from .models import  Order, Coupon, Checkout, TrackShipment, Refund
#
#
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')  # Filter by status and creation date
    search_fields = ('customer__user__username', 'status')  # Search by customer username and order status
    ordering = ('-created_at',)  # Orders by latest orders first
#
#
@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'payment_status', 'shipping_address')
    list_filter = ('payment_status',)  # Filter by payment status
    search_fields = ('customer__user__username', 'order__id')  # Search by customer username and order ID
    ordering = ('customer',)
#
#
@admin.register(TrackShipment)
class TrackShipmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'tracking_number', 'carrier', 'status', 'estimated_delivery')
    list_filter = ('carrier', 'status')  # Filter by carrier and status
    search_fields = ('tracking_number', 'order__id')  # Search by tracking number and order ID
    ordering = ('-estimated_delivery',)  # Orders by closest estimated delivery date
#
#
@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('order', 'status', 'reason', 'created_at')
    list_filter = ('status', 'created_at')  # Filter by refund status and creation date
    search_fields = ('order__id', 'status', 'reason')  # Search by order ID, refund status, and reason
    ordering = ('-created_at',)  # Orders by latest refunds first
