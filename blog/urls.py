from django.urls import path
from .views import PostList,PostDetails
from .api_view import Blog_list,Blog_details,Blog_search

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(),name='BlogList'),
    path('<slug:slug>', PostDetails.as_view(),name='BlogDetails'),


    # API_URLS
    path('api/list', Blog_list,name='BlogAPIList'),
    path('api/<int:pk>', Blog_details,name='BlogAPIDetail'),
    path('api/<str:query>', Blog_search,name='Blog_search'),


]