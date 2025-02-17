# filepath: receptionists/admin.py
from django.contrib import admin
from .models import Receptionist

admin.site.register(Receptionist)