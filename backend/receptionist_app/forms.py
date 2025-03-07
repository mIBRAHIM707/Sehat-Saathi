from django import forms
from hms_app.models import Patient  # Import Patient model

class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['reg_num', 'first_name', 'last_name', 'gender', 'date_of_birth', 'contact_number'] # Include the fields you want in the registration form
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}), # HTML5 date input
        }
        labels = { # Optional: Customize field labels if needed
            'reg_num': 'Registration Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'date_of_birth': 'Date of Birth',
            'contact_number': 'Contact Number',
        }