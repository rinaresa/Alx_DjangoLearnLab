# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, home  # ✅ include 'home'

urlpatterns = [
    path('', home, name='home'),  # ✅ add this to handle the root URL
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
