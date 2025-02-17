# filepath: appointments/models.py
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='scheduled',
    )

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.appointment_date}"