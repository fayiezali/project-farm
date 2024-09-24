from django.contrib import admin
from .models import  Review
#
#
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')  # Filter by rating and creation date
    search_fields = ('customer__user__username', 'product__title')  # Search by customer username and product title
    ordering = ('-created_at',)  # Orders by latest reviews first
