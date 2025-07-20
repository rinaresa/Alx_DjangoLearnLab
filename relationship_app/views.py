from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view for listing all books
def book_list(request):
    books = Book.objects.all().select_related('author')  # Optimized query
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # No need to add books - they're accessible via library.books.all in template
        return context