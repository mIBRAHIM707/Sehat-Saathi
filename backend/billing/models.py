# billing/models.py
from django.db import models # type: ignore
from patients.models import Patient
from appointments.models import Appointment

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=255, blank=True)
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Overdue', 'Overdue'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unpaid')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Bill for {self.patient} on {self.bill_date}"