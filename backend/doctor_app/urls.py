from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('patients/', views.doctor_patient_list, name='doctor_patient_list'),
]