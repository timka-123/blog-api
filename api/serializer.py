from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    full_post = serializers.CharField()
    author = serializers.CharField()

    class Meta:
        model = Post
        fields = ['title', 'full_post', 'author']
