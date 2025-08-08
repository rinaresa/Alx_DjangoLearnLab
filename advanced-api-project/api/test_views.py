from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.list_url = reverse('book-list')

    def test_get_book_detail(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    # Add more test methods here
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
    def test_get_book_detail(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")
    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_delete_book(self):
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        Book.objects.create(title='Another Book', publication_year=2021, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
        
    def test_requires_authentication(self):
        client = APIClient()  # unauthenticated client
        response = client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401 depending on setup
