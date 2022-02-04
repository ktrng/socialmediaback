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
            'posts'

        )
