# posts/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from accounts.models import Follow
from .models import Post

User = get_user_model()

class FeedTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="pass")
        self.bob = User.objects.create_user(username="bob", password="pass")
        self.charlie = User.objects.create_user(username="charlie", password="pass")
        # bob and charlie create posts
        Post.objects.create(author=self.bob, title="Bob 1", content="b")
        Post.objects.create(author=self.charlie, title="Charlie 1", content="c")
        # alice follows bob only
        Follow.objects.create(follower=self.alice, following=self.bob)
        self.client.login(username="alice", password="pass")

    def test_feed_shows_followed_users_posts(self):
        url = reverse("feed")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        results = response.data.get("results", [])
        # Should contain bob's post only
        titles = [p["title"] for p in results]
        self.assertIn("Bob 1", titles)
        self.assertNotIn("Charlie 1", titles)
