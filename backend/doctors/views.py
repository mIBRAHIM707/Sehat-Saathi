# doctors/views.py
from django.shortcuts import render, get_object_or_404 #type: ignore
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})