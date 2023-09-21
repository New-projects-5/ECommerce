from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'updated_time', 'is_available']

admin.site.register(Product, ProductAdmin),
admin.site.register(Category)
