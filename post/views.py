from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from post.models import Post
from .permissons import IsAuthorOrAdmin, IsAuthor


# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.PostListSerializers
        return serializers.PostCreateSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return serializers.PostCreateSerializers
        return serializers.PostDetailSerializers

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdmin(),
        elif self.request.method in ('PUT', 'PATCH'):
            return IsAuthor(),
        return permissions.AllowAny(),




