from django.urls import path
from .views import home, book_list, library_detail, LibraryDetailView

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='book-list'),
    path('library/<int:pk>/fbv', library_detail, name='library-detail-fbv'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]