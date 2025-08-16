from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
      # ModelSerializer is a shortcut to automatically create a serializer
      # with fields that correspond to your model.
      class Meta:
            model=Post
            fields='__all__'