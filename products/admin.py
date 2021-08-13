from django.contrib import admin
from .models import Product, Category, Option


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'friendly_name',
        'name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'has_options',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Option)
