from django.urls import path
from . import views

urlpatterns = [
    # placeholder path
    path('', views.placeholder, name='placeholder'),
]
