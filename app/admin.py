from django.contrib import admin
from .models import Category, Product, Color

admin.site.register(Category)
admin.site.register(Color)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'end_date']
    list_display_links = ['id', 'name']
    list_filter = ['price', 'date', 'end_date', 'category']
    search_fields = ['title', 'category', 'discription']

# Register your models here.
