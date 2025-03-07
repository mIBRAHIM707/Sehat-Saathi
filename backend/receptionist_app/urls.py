from django.urls import path
from . import views

urlpatterns = [
    path('register-patient/', views.receptionist_patient_registration_view, name='receptionist_patient_registration'),
]