from rest_framework import serializers
from django.conf import settings
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username",)

class CommentSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", queryset=User.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Comment
        fields = ("id", "post", "content", "author", "author_id", "created_at", "updated_at")
        read_only_fields = ("id", "author", "created_at", "updated_at")

    def create(self, validated_data):
        # author will usually be set in view.perform_create
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    # allow author_id for admin-ish endpoints (optional)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", queryset=User.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Post
        fields = ("id", "author", "author_id", "title", "content", "created_at", "updated_at", "comments")
        read_only_fields = ("id", "author", "created_at", "updated_at", "comments")

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be blank.")
        return value
