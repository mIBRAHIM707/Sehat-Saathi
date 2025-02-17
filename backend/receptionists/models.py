# filepath: receptionists/models.py
from django.db import models
from accounts.models import User  # Import the User model

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Link to User model
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Emp ID: {self.employee_id})"