from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library, Author

def home(request):
    """Home page view"""
    libraries = Library.objects.all()
    return render(request, 'relationship_app/home.html', {'libraries': libraries})

def book_list(request):
    """Book list view"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, pk):
    """Function-based view for library details"""
    library = Library.objects.get(pk=pk)
    books = library.books.all()  # Using the related_name 'books'
    return render(request, 'relationship_app/library_detail.html', {
        'library': library,
        'books': books
    })

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books in this library using the many-to-many relationship
        context['books'] = self.object.books.all()
        return context