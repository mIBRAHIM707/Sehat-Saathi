# billing/views.py
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Bill

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

def bill_detail(request, bill_id):
    bill = get_object_or_404(Bill, pk=bill_id)
    return render(request, 'billing/bill_detail.html', {'bill': bill})