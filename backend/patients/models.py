from django.db import models # type: ignore
from appointments.models import Appointment
from doctors.models import Doctor
# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)  # Allow null/blank
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    reg_no = models.CharField(max_length=255, unique=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.reg_no})"
    
class Medical_Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    record_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Record for {self.patient} on {self.record_date}"

class Prescription(models.Model):
    record = models.ForeignKey(Medical_Record, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Prescription for {self.record.patient} - {self.drug_name}"

class LabTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    test_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    results = models.TextField(blank=True)
    STATUS_CHOICES = [
        ('Ordered', 'Ordered'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ordered')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Lab Test: {self.test_name} for {self.patient}"