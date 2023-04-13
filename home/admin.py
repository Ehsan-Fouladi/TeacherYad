from django.contrib import admin
from . import models

admin.site.site_header = "معلم یاد"
admin.site.index_title = "Welcome to Admin TeacherYad"

@admin.register(models.Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    list_filter = ("name",)
    list_editable = ("email",)