from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Step 1: Set up filtering
    filter_backends = [
        DjangoFilterBackend,       # for field filtering
        filters.SearchFilter,      # for search functionality
        filters.OrderingFilter,    # for ordering results
    ]
    
    # Fields to filter by (exact match)
    filterset_fields = [
        'title', 
        'author', 
        'publication_year',
        # add any other fields you want to filter by
    ]
    
    # Step 2: Implement search functionality
    search_fields = [
        'title',          # will search in title field
        'author',         # will search in author field
        # you can also do related lookups or partial matches:
        # '^title',       # starts-with search
        # '=title',       # exact match
        # '@title',       # full-text search (if supported)
    ]
    
    # Step 3: Configure ordering
    ordering_fields = [
        'title',
        'author',
        'publication_year',
        'created_at',
        # add any other fields you want to allow ordering by
    ]
    
    # Default ordering if none is specified
    ordering = ['title']