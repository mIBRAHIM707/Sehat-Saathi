# Sehat-Saathi/backend/urls.py
from django.contrib import admin #type: ignore
from django.urls import path, include #type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('patients.urls')),  # Include the patients app's URLs
    path('', include('doctors.urls')),  # Include the doctors app's URLs
    path('', include('appointments.urls')),  # Include the appointments app's URLs
    path('', include('billing.urls')),  # Include the billing app's URLs
]