from django.contrib import admin

from product.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryManager(admin.ModelAdmin):
    list_display = ('id', 'created', 'name',)
    search_fields = ('name',)
    list_filter = ('created',)


@admin.register(SubCategory)
class SubCategoryManager(admin.ModelAdmin):
    list_display = ('id', 'created', 'name', 'category', )
    search_fields = ('name',)
    list_filter = ('category', 'created',)


@admin.register(Product)
class ProductManager(admin.ModelAdmin):
    list_display = ('id', 'created', 'name', 'sub_category', )
    search_fields = ('name',)
    list_filter = ('sub_category', 'created',)

