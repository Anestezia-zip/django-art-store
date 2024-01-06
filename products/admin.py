from django.contrib import admin
from .models import Product, Category, ProductRating, Wishlist
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'image')
    ordering = ('sku',)
    summernote_fields = ('description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductRating)
admin.site.register(Wishlist)
