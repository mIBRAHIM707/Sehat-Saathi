# appointments/admin.py
from django.contrib import  admin	# type: ignore
from .models import Appointment

admin.site.register(Appointment)