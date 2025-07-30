from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: keep the ListAPIView route for comparison or basic read-only access
    path('books/', BookList.as_view(), name='book-list'),

    # Include ViewSet-based routes
    path('', include(router.urls)),
]
