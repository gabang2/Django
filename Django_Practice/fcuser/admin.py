from django.contrib import admin


# Register your models here.
from fcuser.models import Fcuser


class FcuserAmdin(admin.ModelAdmin):
    list_display = ("email",)


admin.site.register(Fcuser, FcuserAmdin)
