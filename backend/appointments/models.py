# appointments/models.py
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"