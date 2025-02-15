# patients/urls.py
from django.urls import path #type: ignore	
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<str:reg_no>/', views.patient_detail, name='patient_detail'),
]