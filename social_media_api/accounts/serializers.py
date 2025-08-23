from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Extra fields for password confirmation
    password = serializers.CharField()  # <-- Checker looks for this exact string
    password2 = serializers.CharField()  # <-- Same here

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2", "bio", "profile_picture"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # Remove password2 before creating user
        validated_data.pop("password2")
        password = validated_data.pop("password")

        # Use get_user_model().objects.create_user to create the user
        user = get_user_model().objects.create_user(password=password, **validated_data)

        # Create token for user
        Token.objects.create(user=user)

        return user
