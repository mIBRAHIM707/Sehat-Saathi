from django.shortcuts import render
from .forms import AppointmentBookingForm # Import the form

def patient_appointment_booking_view(request):
    """View for patients to book appointments (basic form display)."""
    form = AppointmentBookingForm() # Create an instance of the form
    context = {'form': form}
    return render(request, 'patient_app/patient_appointment_booking.html', context)