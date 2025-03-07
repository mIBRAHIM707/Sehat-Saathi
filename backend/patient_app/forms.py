from django import forms
from hms_app.models import Doctor  # Import Doctor model

class AppointmentBookingForm(forms.Form):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Select Doctor")
    appointment_date = forms.DateTimeField(label="Preferred Date and Time", widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})) # HTML5 datetime-local input
    reason = forms.CharField(widget=forms.Textarea, label="Reason for Appointment")