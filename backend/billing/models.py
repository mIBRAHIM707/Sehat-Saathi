# filepath: billing/models.py
from django.db import models
from patients.models import Patient
from appointments.models import Appointment

class Billing(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)  # Optional appointment
    billing_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('cash', 'Cash'),
            ('credit_card', 'Credit Card'),
            ('insurance', 'Insurance'),
            ('other', 'Other'),
        ],
        default='cash',
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('partially_paid', 'Partially Paid'),
            ('refunded', 'Refunded'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending',
    )
    notes = models.TextField(blank=True, null=True)  # Additional notes or details
    insurance_provider = models.CharField(max_length=100, blank=True, null=True)  # If paid by insurance
    insurance_policy_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Bill #{self.bill_id} for {self.patient} - Amount: {self.amount} - Status: {self.status}"