"""
URL configuration for hms_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Import built-in auth views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor_app.urls')),
    path('patient/', include('patient_app.urls')),
    path('receptionist/', include('receptionist_app.urls')), # Add this line for receptionist app URLs

    
    path('login/', auth_views.LoginView.as_view(), name='login'), # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Logout URL
]