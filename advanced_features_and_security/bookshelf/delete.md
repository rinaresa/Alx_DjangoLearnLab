### DELETE OPERATION

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# <QuerySet []>
