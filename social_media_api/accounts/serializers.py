from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for listing and retrieving user details.
    """
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Automatically creates a Token for the new user.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        # Create user with hashed password
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        # Generate token for the new user
        Token.objects.create(user=user)
        return user
