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
