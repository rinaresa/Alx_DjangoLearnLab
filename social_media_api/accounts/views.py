from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Follow, CustomUser  # ✅ Import CustomUser
from .serializers import UserSerializer


# ✅ Explicitly set CustomUser instead of get_user_model()
User = CustomUser


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


# ✅ Register a new user (explicitly uses CustomUser.objects.all())
class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ✅ Login view (returns token)
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })


# ✅ Authenticated user profile
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# ------------------ SERIALIZERS ------------------

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "password2", "bio", "profile_picture"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(password=password, **validated_data)
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "bio", "profile_picture"]


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["bio", "profile_picture"]
        extra_kwargs = {
            'bio': {'required': False},
            'profile_picture': {'required': False},
        }
