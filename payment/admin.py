from django.contrib import admin
from .models import  Coupon
#
#
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'active', 'expires_at')
    list_filter = ('active', 'expires_at')  # Filter by active status and expiration date
    search_fields = ('code',)  # Search by coupon code
    ordering = ('expires_at',)
