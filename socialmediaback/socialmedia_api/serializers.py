from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'email',
            'password',
            'first_name',
            'middle_name',
            'last_name',
            'dob',
            'friends',
            'posts',
            'comments'
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post_id',
            'author',
            'body',
            'comments',
            'likes'
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'comment_id',
            'author',
            'postedto',
            'body',
            'likes'
        )
