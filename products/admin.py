from django.contrib import admin
from .models import Product, Category, ProductRating, Wishlist
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'id', 'sku', 'category', 'price', 'image')
    ordering = ('id',)
    summernote_fields = ('description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_name', 'score')

    def get_product_name(self, obj):
        return obj.product.name
    get_product_name.short_description = 'Product Name'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(Wishlist)
