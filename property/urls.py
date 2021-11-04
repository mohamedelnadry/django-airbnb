from django.urls import path
from .views import PropertyList,PropertyDetails,property_new
from django.conf import settings
from django.conf.urls.static import static
from .api_view import PropertyListAPI,PropertyDetailAPI

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(),name='propertyList'),
    path('new', property_new.as_view(),name='PropertyNew'),
    path('<slug:slug>', PropertyDetails.as_view(),name='propertyDetail'),

    # APU_URLS
    path('api/list', PropertyListAPI.as_view(),name='PropertyListAPI'),
    path('api/<int:pk>', PropertyDetailAPI.as_view(),name='PropertyDetailAPI'),

]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)