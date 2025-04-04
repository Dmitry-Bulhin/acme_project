from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description'
    )
# ...и регистрируем её в админке:
# admin.site.register(Category)
admin.site.register(Birthday)
