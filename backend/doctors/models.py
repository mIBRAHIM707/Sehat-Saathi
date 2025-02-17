# filepath: doctors/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from django.core.mail import send_mail
import uuid

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.specialization})"

@receiver(post_save, sender=Doctor)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Generate a random password
        random_password = uuid.uuid4().hex[:8]  # 8 character random password

        # Create the user
        user = User.objects.create_user(
            username=instance.employee_id,
            password=random_password,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            user_type='doctor',
        )

        # Send email to user with temporary password
        send_mail(
            'Your Account Has Been Created',
            f'Your account has been created with username: {instance.employee_id} and temporary password: {random_password}. Please change your password after logging in.',
            'ibrahimclash707@gmail.com',  # Replace with your sending email
            [instance.email],
            fail_silently=False,
        )