# query_samples.py
from .models import Author, Book, Library, Librarian

def books_by_author(author_name):
    authors = Author.objects.filter(name=author_name)
    return Book.objects.filter(author__in=authors)

def books_in_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    books = Book.objects.filter(library__in=libraries).distinct()
    return books


def librarian_of_library(library_name):
    libraries = Library.objects.filter(name=library_name)
    librarians = []
    for library in libraries:
        try:
            librarians.append(library.librarian)
        except Librarian.DoesNotExist:
            continue
    return librarians
