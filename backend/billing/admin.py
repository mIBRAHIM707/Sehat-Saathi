# filepath: billing/admin.py
from django.contrib import admin
from .models import Billing

admin.site.register(Billing)