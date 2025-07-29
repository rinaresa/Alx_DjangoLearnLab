# bookshelf/urls.py

from django.urls import path
from .views import book_list, create_book, edit_book, delete_book

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/create/', create_book, name='create_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
