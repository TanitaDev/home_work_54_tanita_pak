from django.contrib import admin


from webapp.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'create_at']
    list_filter = ['name', 'category']
    search_fields = ['name', 'description']
    fields = ['name', 'create_at', 'description', 'image', 'category', 'price']
    readonly_fields = ['create_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
