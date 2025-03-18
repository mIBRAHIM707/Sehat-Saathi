from django.shortcuts import render, redirect
from .forms import AppointmentBookingForm
from hms_app.models import Appointment, Patient # Import Patient model as well
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Import login_required

@login_required # Apply login_required decorator
def patient_appointment_booking_view(request):
    """View for patients to book appointments, handling form submission."""
    try:
        # **TEMPORARY FIX:** Fetch the first patient for now (replace with actual user association later)
        test_patient = Patient.objects.first() # Get the first Patient object from the database
        if not test_patient:
            messages.error(request, "No patients available in the system to book appointment. Please register a patient first (This is a temporary test setup).")
            form = AppointmentBookingForm() # Create an empty form to re-render
            context = {'form': form}
            return render(request, 'patient_app/patient_appointment_booking.html', context)


        if request.method == 'POST':
            form = AppointmentBookingForm(request.POST)
            if form.is_valid():
                # Get data from the form
                doctor = form.cleaned_data['doctor']
                appointment_date = form.cleaned_data['appointment_date']
                reason = form.cleaned_data['reason']

                # Create an Appointment object
                appointment = Appointment(
                    patient=test_patient, # **Assign the fetched patient here**
                    doctor=doctor,
                    appointment_date=appointment_date,
                    reason=reason,
                    status='Scheduled'
                )
                appointment.save()

                messages.success(request, "Appointment booked successfully!")
                return redirect('patient_appointment_booking')
            else:
                messages.error(request, "Please correct the errors below.")
        else: # GET request
            form = AppointmentBookingForm()

    except Exception as e: # Catch potential exceptions like database errors
        messages.error(request, f"An error occurred while booking appointment: {e}") # Display a general error message
        form = AppointmentBookingForm() # Re-initialize form to prevent issues in template rendering

    context = {'form': form}
    return render(request, 'patient_app/patient_appointment_booking.html', context)