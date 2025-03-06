from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    reg_num = models.CharField(max_length=20, unique=True, verbose_name="Registration Number")
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ], verbose_name="Gender")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Contact Number")
    email = models.EmailField(verbose_name="Email", blank=True, null=True) # Keep EmailField for validation, but make it optional for now
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Reg. No: {self.reg_num})"
    
    def save(self, *args, **kwargs):
        # Auto-generate email if reg_num is set and email is not already provided
        if self.reg_num and not self.email:
            self.email = f"{self.reg_num}@giki.edu.pk"
        elif self.reg_num and self.email:
            expected_email = f"{self.reg_num}@giki.edu.pk"
            if self.email != expected_email:
                try:
                    validate_email(self.email) # Validate provided email if different from auto-generated one
                except ValidationError:
                    pass # Let the user provide any valid email if they want to override auto-generation, or you can raise an error here if you want to enforce the pattern.

        super().save(*args, **kwargs) # Call the original save method to save the model

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    specialization = models.CharField(max_length=100, verbose_name="Specialization")
    department = models.CharField(max_length=100, verbose_name="Department")
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Contact Number")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', verbose_name="Patient")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments', verbose_name="Doctor")
    appointment_date = models.DateTimeField(verbose_name="Appointment Date & Time")
    reason = models.TextField(verbose_name="Reason for Appointment")
    status = models.CharField(max_length=20, choices=[
        ('Scheduled', 'Scheduled'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ], default='Scheduled', verbose_name="Status")

    def __str__(self):
        return f"Appointment #{self.appointment_id} - Patient: {self.patient}, Doctor: {self.doctor}"

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"

class Billing(models.Model):
    bill_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bills', verbose_name="Patient")
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True, related_name='bills', verbose_name="Appointment")
    bill_date = models.DateTimeField(auto_now_add=True, verbose_name="Bill Date")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount")
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
        ('Cancelled', 'Cancelled'),
    ], default='Pending', verbose_name="Status")
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name="Payment Date")
    payment_method = models.CharField(max_length=50, blank=True, null=True, verbose_name="Payment Method")
    invoice_number = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name="Invoice Number")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")

    def __str__(self):
        return f"Bill #{self.bill_id} - Patient: {self.patient}, Amount: {self.amount}, Status: {self.status}"

    class Meta:
        verbose_name = "Bill"
        verbose_name_plural = "Bills"