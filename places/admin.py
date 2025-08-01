from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ("get_preview",)
    fields = ("image", "get_preview", "position")
    ordering = ("position",)

    def get_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 300px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    get_preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["place", "position", "preview"]
    readonly_fields = ["preview"]
    ordering = ["place", "position"]
    raw_id_fields = ["place"]

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 200px; max-width: 300px;" />',
                obj.image.url,
            )
        return "Нет изображения"
