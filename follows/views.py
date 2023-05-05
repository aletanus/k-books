from rest_framework import generics , status
from rest_framework.response import Response 
from follows.models import Follow
from follows.serializers import FollowSerializer
from users.models import Users
from books.models import Book
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

       
class FollowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer



