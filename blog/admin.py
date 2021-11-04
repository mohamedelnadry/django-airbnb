from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
from .models import Post,Category

class Postadmin(SummernoteModelAdmin):
    summernote_fields = '__all__'



admin.site.register(Post,Postadmin)
admin.site.register(Category)
