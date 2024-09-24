from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'city', 'postal_code')  # Fields displayed in the list view
    list_filter = ('city',)  # Filter customers by city
    search_fields = ('user__username', 'phone_number', 'city')  # Search by username, phone, and city
    ordering = ('user',)  # Orders by username
