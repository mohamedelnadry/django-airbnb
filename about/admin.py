from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from . import models

class aboutadmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(models.About,aboutadmin)
admin.site.register(models.FAQ)
admin.site.register(models.INFO)
