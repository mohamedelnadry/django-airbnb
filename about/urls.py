from django.urls import path
from .views import QustionDetail
app_name = 'about'

urlpatterns = [
    path('', QustionDetail.as_view(),name='FAQDeatil'),
    # path('<slug:slug>', PostDetails.as_view(),name='BlogDetails'),

]