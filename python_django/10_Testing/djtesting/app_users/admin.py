from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'date_of_birth', 'telephone_number', 'about_myself']
    search_fields = ['user', 'city']


admin.site.register(Profile, ProfileAdmin)
