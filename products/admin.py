from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'parent')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
