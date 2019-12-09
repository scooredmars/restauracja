from django.contrib import admin

from .models import Categories, Gallery, Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "category",
        "price",
        "size",
    )

    list_select_related = ("category",)

    list_filter = (("category", admin.RelatedOnlyFieldListFilter),)


admin.site.register(Categories)
admin.site.register(Gallery)
