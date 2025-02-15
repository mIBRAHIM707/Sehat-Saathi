# billing/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('bills/', views.bill_list, name='bill_list'),
    path('bills/<int:bill_id>/', views.bill_detail, name='bill_detail'),
]