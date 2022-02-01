from django.contrib import admin
from .models import Advertisement,Autor,Category,Type
# Register your models here.

@admin.register(Advertisement,Autor,Category,Type)
class AdvertisementAdmin(admin.ModelAdmin):
    pass
