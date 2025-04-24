from django.contrib import admin
from .models import AllProducts, Category
from django.utils.html import mark_safe


# Register your models here.

@admin.register(AllProducts)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image', 'created_at', 'updated_at', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'price', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    ordering = ('-updated_at',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img = "{obj.image.url}"width="50" height="50"/>')
        return "No Image"
    image_tag.short_description = 'Image'





# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)