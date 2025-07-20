from django.urls import path
from .views import book_list, home, LibraryDetailView  # Make sure all views are imported

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]