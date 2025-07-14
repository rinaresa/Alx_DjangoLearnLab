from django.contrib import admin
from django.urls import path, include
from relationship_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('relationship_app.urls')),
]
