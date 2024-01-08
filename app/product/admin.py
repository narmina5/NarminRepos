from django.contrib import admin

from .models import (Category, Product, ProductItem,
                     ProductType, Color, Size, Brand, Comment)


class InlineSizeAdmin(admin.TabularInline):
    model = Size
    extra = 1


class InlineColorAdmin(admin.TabularInline):
    model = Color
    extra = 1


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = (InlineSizeAdmin, InlineColorAdmin)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductItem)
# admin.site.register(Color)
# admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Comment)
