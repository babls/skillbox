from django.contrib import admin

from .models import Shop, Product, Profile, History_shopping, ListProductShop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']


class HistoryShoppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'product', 'shop', 'date_of_shopping', 'count', 'user')
    list_filter = ['status', 'product', 'shop']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ['name', 'category']


class ListProductShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'product', 'amount')
    list_filter = ['shop', 'product', 'amount']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance', 'status')
    list_filter = ['user', 'status']


admin.site.register(Shop, ShopAdmin)
admin.site.register(History_shopping, HistoryShoppingAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ListProductShop, ListProductShopAdmin)
admin.site.register(Profile, ProfileAdmin)
