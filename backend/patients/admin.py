# patients/admin.py
from django.contrib import admin # type: ignore
from .models import Patient, Medical_Record, Prescription, LabTest

admin.site.register(Patient)
admin.site.register(Medical_Record)
admin.site.register(Prescription)
admin.site.register(LabTest)