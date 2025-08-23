from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import Follow
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUnfollowView(APIView):
    """
    POST /api/auth/follow/<user_id>/  -> follow user_id
    DELETE /api/auth/follow/<user_id>/ -> unfollow user_id
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        target = get_object_or_404(User, pk=user_id)
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target)
        if created:
            return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Already following."}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        target = get_object_or_404(User, pk=user_id)
        deleted, _ = Follow.objects.filter(follower=request.user, following=target).delete()
        if deleted:
            return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "You were not following this user."}, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()

# Register a new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# Login view (returns token)
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })


# Authenticated user profile
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user





class RegisterSerializer(serializers.ModelSerializer):
    # Extra fields for password confirmation
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture"]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["bio", "profile_picture"]
        extra_kwargs = {
            'bio': {'required': False},
            'profile_picture': {'required': False},
        }