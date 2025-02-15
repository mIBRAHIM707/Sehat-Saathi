# patients/views.py
from django.shortcuts import render, get_object_or_404 #type: ignore	
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, reg_no):
    patient = get_object_or_404(Patient, reg_no=reg_no)
    return render(request, 'patients/patient_detail.html', {'patient': patient})