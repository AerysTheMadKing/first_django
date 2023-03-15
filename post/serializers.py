from rest_framework import serializers

from category.models import Category
from .models import Post


class PostListSerializers(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'category',
                  'preview', 'owner_username', 'category_name')


class PostCreateSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'preview')


class PostDetailSerializers(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Post
        fields = '__all__'

