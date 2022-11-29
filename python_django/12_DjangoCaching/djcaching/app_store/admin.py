from django.contrib import admin

from .models import Shop, Product, Action_and_offer, Profile, History_shopping


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']


class HistoryShoppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_shopping', 'count', 'total', 'user')
    list_filter = ['date_of_shopping']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ['name', 'category']


class ActionAndOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'text_action', 'shop')
    list_filter = ['name', 'type', 'shop']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'balance', 'city', 'telephone_number', 'about_myself')
    list_filter = ['user', 'telephone_number', 'city']


admin.site.register(Shop, ShopAdmin)
admin.site.register(History_shopping, HistoryShoppingAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Action_and_offer, ActionAndOfferAdmin)
admin.site.register(Profile, ProfileAdmin)
