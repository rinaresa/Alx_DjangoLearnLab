from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view for book list
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Function-based view for home page
def home(request):
    return render(request, 'relationship_app/home.html')

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_details.html'
    context_object_name = 'library'