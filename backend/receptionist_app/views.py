from django.shortcuts import render
from .forms import PatientRegistrationForm # Import the form

def receptionist_patient_registration_view(request):
    """View for receptionists to register new patients (basic form display)."""
    form = PatientRegistrationForm() # Create an instance of the form
    context = {'form': form}
    return render(request, 'receptionist_app/receptionist_patient_registration.html', context)