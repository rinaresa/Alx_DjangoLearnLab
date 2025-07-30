from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for basic ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Routes from the ViewSet
    path('', include(router.urls)),

    # Token auth endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
