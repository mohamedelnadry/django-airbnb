from django import forms
from django.forms import fields
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class userCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



class profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone_number','address']