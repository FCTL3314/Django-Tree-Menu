from django.contrib import admin

from menus.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
