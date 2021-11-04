from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('property/',include('property.urls',namespace='property')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('about/',include('about.urls',namespace='about')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace='accounts'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
X_FRAME_OPTIONS = 'SAMEORIGIN'
