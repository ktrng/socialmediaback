from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework import generics

from .serializers import UserSerializer
from .models import User

from .serializers import PostSerializer
from .models import Post

from .serializers import CommentSerializer
from .models import Comment

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    querset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
