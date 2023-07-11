from django.contrib import admin

# Register your models here.
from user.models import FcUser


class FcUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'password')


admin.site.register(FcUser, FcUserAdmin)
