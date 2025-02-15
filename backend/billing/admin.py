# billing/admin.py
from django.contrib import admin # type: ignore
from .models import Bill

admin.site.register(Bill)