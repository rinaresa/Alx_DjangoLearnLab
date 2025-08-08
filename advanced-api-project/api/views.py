from django_filters import rest_framework
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import OrderingFilter
from .models import Book
from .serializers import BookSerializer


class BookFilter(rest_framework.FilterSet):
    title = rest_framework.CharFilter(lookup_expr='icontains')
    author__name = rest_framework.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = rest_framework.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author__name', 'publication_year']


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, OrderingFilter]
    filterset_class = BookFilter
    ordering_fields = ['title', 'publication_year']
