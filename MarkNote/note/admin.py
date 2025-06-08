from django.contrib import admin
from .models import Note ,Comment
# Register your models here.
admin.site.register(Comment)
@admin.register(Note)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","slug","status","publish")
    list_filter = ("status",)
    search_fields = ("title","body")
    date_hierarchy = "publish"
    list_editable = ('status',)