from django.contrib import admin

from .models import TypeHouse, CountRooms, House, News


class TypeHouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name']


class CountRoomsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name']


class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Address', 'Price', 'TypeHouse', 'CountRooms')
    list_filter = ['TypeHouse', 'CountRooms']


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'House', 'is_published', 'description', 'published_at')
    list_filter = ['is_published', 'published_at']


admin.site.register(TypeHouse, TypeHouseAdmin)
admin.site.register(CountRooms, CountRoomsAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(News, NewsAdmin)
