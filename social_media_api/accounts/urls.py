# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUnfollowView  # ensure these exist

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<int:user_id>/", FollowUnfollowView.as_view(), name="follow-unfollow"),
    path("unfollow/<int:user_id>/", FollowUnfollowView.as_view(), name="unfollow"),
]
