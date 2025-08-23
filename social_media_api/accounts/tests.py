# accounts/tests.py
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user(username="alice", password="pass")
        self.bob = User.objects.create_user(username="bob", password="pass")
        self.client.login(username="alice", password="pass")

    def test_follow_and_unfollow(self):
        url = reverse("follow-unfollow", args=[self.bob.id])
        # follow
        response = self.client.post(url)
        self.assertIn(response.status_code, (201, 200))
        # unfollow
        response = self.client.delete(url)
        self.assertIn(response.status_code, (204, 200, 400))
