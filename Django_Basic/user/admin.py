from django.contrib import admin

# Register your models here.
from user.models import FcUser


class FcUserAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email', 'password')


admin.site.register(FcUser, FcUserAdmin)
