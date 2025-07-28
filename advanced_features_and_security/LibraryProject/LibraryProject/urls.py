from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from relationship_app.views import role_based_dashboard  # ✅ Import here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('book_list')),  # Redirect root to /books/
    path('', include('relationship_app.urls')),
    path('dashboard/', role_based_dashboard, name='role_dashboard'),
]
