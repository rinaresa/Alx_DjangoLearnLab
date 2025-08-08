from django_filters import rest_framework as filters  # already added ✅
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author__name = filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author__name', 'publication_year']


# GET /books/?title=&author__name=&publication_year=
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
