from django.contrib import admin

from apps.shortcut.models import Shortcut


# Register your models here.
@admin.register(Shortcut)
class ShortcutAdmin(admin.ModelAdmin):
    search_fields = ("title", "link")
    list_display = ("title", "link")
