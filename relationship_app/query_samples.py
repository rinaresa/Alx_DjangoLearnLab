from relationship_app.models import Author, Book, Library, Librarian

# Show all libraries and their books
libraries = Library.objects.all()
print("All Libraries:", list(libraries))
for lib in libraries:
    print(f"Library ID: {lib.id}, Books: {list(lib.books.all())}")

# Get books by Chinua Achebe
achebe = Author.objects.filter(name="Chinua Achebe").first()
if achebe:
    books_by_achebe = Book.objects.filter(author=achebe)
    print(f"Books by Chinua Achebe: {list(books_by_achebe)}")
else:
    print("Author 'Chinua Achebe' not found.")

# Find a library that has books
target_library = None
for lib in libraries:
    if lib.books.exists():
        target_library = lib
        break

if target_library:
    print(f"Books in library {target_library.id}: {list(target_library.books.all())}")
    librarian = Librarian.objects.filter(library=target_library).first()
    if librarian:
        print(f"Librarian for {target_library.name}: {librarian.name}")
    else:
        print(f"No librarian assigned to {target_library.name}")
else:
    print("No library with books found.")
