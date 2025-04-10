from django.contrib import admin

from .models import Birthday, Tag


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'tag'
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description'
    )


# ...и регистрируем её в админке:
# admin.site.register(Category)
admin.site.register(Birthday)
admin.site.register(Tag)
