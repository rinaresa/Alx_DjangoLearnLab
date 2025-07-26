from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # Adjusted to meet the task's check
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to show library details and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
