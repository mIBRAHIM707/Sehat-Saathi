# filepath: patients/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from django.core.mail import send_mail
import uuid

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reg_num = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Reg: {self.reg_num})"

    def save(self, *args, **kwargs):
        self.email = f"u{self.reg_num}@giki.edu.pk"
        super().save(*args, **kwargs)

@receiver(post_save, sender=Patient)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Generate a random password
        random_password = uuid.uuid4().hex[:8]  # 8 character random password

        # Create the user
        user = User.objects.create_user(
            username=instance.reg_num,
            password=random_password,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
            user_type='patient',
        )

        # Send email to user with temporary password
        send_mail(
            'Your Account Has Been Created',
            f'Your account has been created with username: {instance.reg_num} and temporary password: {random_password}. Please change your password after logging in.',
            'ibrahimclash707@gmail.com',  # Replace with your sending email
            [instance.email],
            fail_silently=False,
        )