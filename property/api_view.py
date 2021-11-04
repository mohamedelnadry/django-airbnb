from .serializers import PropertySerializer
from .models import Property
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class PropertyListAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset  = Property.objects.all()
    
    serializer_class = PropertySerializer



class PropertyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset  = Property.objects.all()
    serializer_class = PropertySerializer
