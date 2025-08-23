from django.contrib.auth import authenticate, get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ProfileUpdateSerializer,
)

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": UserSerializer(user, context={"request": request}).data,
                "token": token.key,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context={"request": request}).data,
            "token": token.key,
        })


class ProfileView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get the authenticated user's profile"""
        return Response(UserSerializer(request.user, context={"request": request}).data)

    def patch(self, request):
        """Update profile (bio, profile_picture, etc.)"""
        serializer = ProfileUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user, context={"request": request}).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
