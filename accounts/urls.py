# employeetrack/accounts/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('allauth.urls')),  # Correct URL pattern for allauth
]
