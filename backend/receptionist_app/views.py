from django.shortcuts import render, redirect
from .forms import PatientRegistrationForm
from django.contrib import messages # Import messages framework for feedback
from django.contrib.auth.decorators import login_required, permission_required # Import login_required

@login_required # Apply login_required decorator
@permission_required('hms_app.add_patient', raise_exception=True) # Require 'hms_app.add_patient' permission
def receptionist_patient_registration_view(request):
    """View for receptionists to register new patients, handling form submission."""
    if request.method == 'POST': # Check if the request is a POST request (form submission)
        form = PatientRegistrationForm(request.POST) # Create form instance with submitted data
        if form.is_valid(): # Validate the form data
            patient = form.save() # Save the form data to the database (creates a Patient object)
            messages.success(request, f"Patient '{patient.first_name} {patient.last_name}' registered successfully with Reg. No: {patient.reg_num}") # Success message
            return redirect('receptionist_patient_registration') # Redirect to the same registration page (or another page if you prefer)
        else: # Form is invalid
            messages.error(request, "Please correct the errors below.") # Error message
            # Form will be re-rendered with errors automatically
    else: # Request is a GET request (initial form load)
        form = PatientRegistrationForm() # Create an empty form instance

    context = {'form': form}
    return render(request, 'receptionist_app/receptionist_patient_registration.html', context)