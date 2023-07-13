from django.contrib import admin

# Register your models here.
from board.models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')


admin.site.register(Board, BoardAdmin)