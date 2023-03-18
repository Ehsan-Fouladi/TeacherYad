from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("user", "username", "name_field", "is_teacher", 'shoe_image')
    list_filter = ("is_teacher", 'username')
    list_editable = ("username", "is_teacher")

