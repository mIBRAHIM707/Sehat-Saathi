# appointments/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
]