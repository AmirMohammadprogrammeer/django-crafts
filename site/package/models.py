from django.db import models
import django_jalali.db.models as jmodels
# Create your models here.

class Package(models.Model):
    name_package = models.CharField(max_length=255,unique=True,)
    date = jmodels.jDateField()
    duration = models.PositiveIntegerField()
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_package