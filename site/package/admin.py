from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name_package', 'date')
    list_filter = (
        ('date', JDateFieldListFilter),
    )
