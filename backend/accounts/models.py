# filepath: accounts/models.py
from django.db import models 
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('receptionist', 'Receptionist'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='patient')

    def __str__(self):
        return self.username