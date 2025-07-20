from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('books/', views.book_list, name='book-list'),  # Book list
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]