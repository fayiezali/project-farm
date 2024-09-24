from django.contrib import admin
from .models import Category, Product
#
#
@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)
#
#
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'category')
    list_filter = ('category', 'price')  # Filter by category and price
    search_fields = ('title', 'description')  # Search by title and description
    ordering = ('title',)
