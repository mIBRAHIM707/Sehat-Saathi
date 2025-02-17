# filepath: accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import User
from patients.models import Patient
from doctors.models import Doctor
from receptionists.models import Receptionist
from appointments.models import Appointment

@receiver(post_save, sender=User)
def create_user_permissions(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'patient':
            # Create a Patient group if it doesn't exist
            patient_group, created = Group.objects.get_or_create(name='Patient')

            # Assign permissions to the Patient group (example)
            content_type = ContentType.objects.get_for_model(Patient)
            permission = Permission.objects.create(
                codename='can_view_patient_profile',
                name='Can view patient profile',
                content_type=content_type,
            )
            patient_group.permissions.add(permission)

            # Add the user to the Patient group
            instance.groups.add(patient_group)

        elif instance.user_type == 'doctor':
            # Create a Doctor group if it doesn't exist
            doctor_group, created = Group.objects.get_or_create(name='Doctor')

            content_type = ContentType.objects.get_for_model(Doctor)
            permission = Permission.objects.create(
                codename='can_edit_patient_records',
                name='Can edit patient records',
                content_type=content_type,
            )
            doctor_group.permissions.add(permission)

            # Add the user to the Doctor group
            instance.groups.add(doctor_group)

        elif instance.user_type == 'receptionist':
            # Create a Receptionist group if it doesn't exist
            receptionist_group, created = Group.objects.get_or_create(name='Receptionist')

            # Assign permissions to the Receptionist group (example)
            content_type = ContentType.objects.get_for_model(Appointment)
            permission = Permission.objects.create(
                codename='can_create_appointments',
                name='Can create appointments',
                content_type=content_type,
            )
            receptionist_group.permissions.add(permission)

            # Add the user to the Receptionist group
            instance.groups.add(receptionist_group)