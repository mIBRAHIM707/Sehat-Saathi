from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.doctor_patient_list, name='doctor_patient_list'), # Keep this or remove if you wish
    path('schedule/', views.doctor_daily_schedule_view, name='doctor_daily_schedule'), # Add this line
]