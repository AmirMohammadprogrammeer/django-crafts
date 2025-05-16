from django import forms
from .models import Package
import django_jalali.forms as jforms

class FormRegisterPackage(forms.ModelForm):
    date = jforms.jDateField(label="data")

    class Meta:
        model = Package
        fields = ('name_package', 'duration', 'date')
