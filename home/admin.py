from django.contrib import admin
from . import models


@admin.register(models.Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name",)
    list_editable = ("email",)