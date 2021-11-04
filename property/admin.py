from django.contrib import admin
from django.contrib.admin.decorators import register
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Property,PropertyImages,PropertyReview,Category,propertyForm



class propertyadmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Property,propertyadmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(propertyForm)



