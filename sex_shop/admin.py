from django.contrib import admin

from sex_shop.models import Manufacturer, Category, Product, News


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['country']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available_count', 'price', 'category', 'manufacturer')
    list_filter = ['category']


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish_date')

admin.site.register(Category)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(News, NewsAdmin)