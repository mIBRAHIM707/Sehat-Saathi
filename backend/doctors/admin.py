# doctors/admin.py
from django.contrib import admin # type: ignore
from .models import Doctor, Department, DoctorAvailability

admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(DoctorAvailability)