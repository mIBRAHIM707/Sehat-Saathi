# appointments/views.py
from django.shortcuts import render, get_object_or_404 #type: ignore
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})