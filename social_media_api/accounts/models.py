from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="following_rel", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers_rel", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")
        indexes = [
            models.Index(fields=["follower"]),
            models.Index(fields=["following"]),
        ]

    def __str__(self):
        return f"{self.follower} -> {self.following}"



class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True,
    )

    def __str__(self):
        return self.username
