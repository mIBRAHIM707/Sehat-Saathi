from django.shortcuts import render
from hms_app.models import Patient # Import the Patient model

def doctor_patient_list(request):
    """View to display a list of patients for a doctor."""
    patients = Patient.objects.all() # Fetch all Patient objects from the database
    context = {'patients': patients}  # Create a context dictionary to pass data to the template
    return render(request, 'doctor_app/doctor_patient_list.html', context) # Pass the context to render