from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .models import Profile
from .froms import profile_form, user_form,userCreateForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def signUP(request):
    if request.method == "POST":
        userForm = userCreateForm(request.POST)
        if userForm.is_valid():
            userForm.save()
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect(reverse('accounts:myprofile'))

    else:
        userForm = userCreateForm()
    

    return render(request,'profile/singup.html',{'userForm':userForm})




def profile(request):
    profile = Profile.objects.get(user = request.user)
    

    return render(request,'profile/profile.html',{'myprofile':profile})



def profile_edit(request):
    
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        userForm = user_form(request.POST,instance=request.user)
        profileForm = profile_form(request.POST,request.FILES,instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myForm = profileForm.save(commit=False)
            myForm.user = request.user
            myForm.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:myprofile'))
    else:
        userForm = user_form(instance=request.user)
        profileForm = profile_form(instance=profile)
    return render(request,'profile/profile_edit.html',{
        'form_user':userForm,
        'form_profile':profileForm
        })

    