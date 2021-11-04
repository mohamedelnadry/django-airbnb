from django import forms
from django.forms.widgets import DateInput
from .models import propertyForm

class property_form(forms.ModelForm):

    date_from = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))

    class Meta:
        model = propertyForm
        fields = ['name','email','date_from','date_to','guest','children']
  