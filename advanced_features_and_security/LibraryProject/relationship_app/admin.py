from django.contrib import admin

# Register your models here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import UserProfile

@login_required
def admin_dashboard(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.role != 'Admin':
            return HttpResponse("Access Denied: Admins only.", status=403)
    except UserProfile.DoesNotExist:
        return HttpResponse("User profile not found.", status=404)
    
    return HttpResponse("Welcome to the Admin Dashboard")
