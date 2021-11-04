from django.urls import path
from .views import profile_edit,profile,signUP


app_name = 'accounts'


urlpatterns = [
    path('signUP',signUP,name='signUP'),
    path('profileEdit',profile_edit,name='profileEdit'),
    path('profile/',profile,name = 'myprofile')
]