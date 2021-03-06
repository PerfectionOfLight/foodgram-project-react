from django.contrib import admin

from .models import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_filter = (
        'email',
        'username',
    )
    empty_value_display = '-пусто-'
