from django.db import models
from accounts.models import User  # Import the User model


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Link to User model
    reg_num = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True, editable=False)  # Make email non-editable

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Reg: {self.reg_num})"

    def save(self, *args, **kwargs):
        self.email = f"u{self.reg_num}@giki.edu.pk"  # Always generate email
        super().save(*args, **kwargs)