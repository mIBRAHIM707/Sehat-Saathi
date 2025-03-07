from django.urls import path
from . import views

urlpatterns = [
    path('book-appointment/', views.patient_appointment_booking_view, name='patient_appointment_booking'),
]