from django.shortcuts import render
from hms_app.models import Appointment  # Import the Appointment model
from django.contrib.auth.decorators import login_required # Import login_required

@login_required 
def doctor_daily_schedule_view(request):
    """View to display a doctor's daily schedule (initially showing all appointments)."""
    appointments = Appointment.objects.all()  # Fetch all appointments for now
    context = {'appointments': appointments}
    return render(request, 'doctor_app/doctor_daily_schedule.html', context)

def doctor_patient_list(request): # Keep this, or remove if you only want schedule for now
    """View to display a list of patients for a doctor."""
    return render(request, 'doctor_app/doctor_patient_list.html')   