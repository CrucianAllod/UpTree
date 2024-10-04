from django.contrib import admin

from tree.models import MenuItem, Menu

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(Menu)
admin.site.register(MenuItem)