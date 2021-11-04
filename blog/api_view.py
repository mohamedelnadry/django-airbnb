from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .models import Post
from .serializers import Blogserializer
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Blog_list(request):
    BlogList = Post.objects.all()
    serializer = Blogserializer(BlogList,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Blog_details(request,pk):
    try:
        BlogDetails = Post.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = Blogserializer(BlogDetails)
    return Response(serializer.data)



@api_view(['GET'])  
def Blog_search(request,query):
    Blogsearch = Post.objects.filter(Q(title__contains=query) | Q(description__contains=query))
    serializer = Blogserializer(Blogsearch,many=True)
    return Response(serializer.data)
