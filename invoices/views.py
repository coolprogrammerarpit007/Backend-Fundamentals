from django.shortcuts import render
from .models import Invoice
from datetime import date
from django.http import JsonResponse

# Create your views here.

current_date = date.today().isoformat()


def create_inoice(request):
    Invoice.objects.create(customer_name="Pankaj Tripathi",invoice_number="LWP7854",invoice_amount=25000,date_created=current_date,is_paid=False)
    
    return render(request,"home.html",{})

def all_invoices(request):
    all_invoices = Invoice.objects.all()
    return all_invoices


def show(request):
    invoice = Invoice.objects.filter(invoice_number="LWP7854")
    return invoice


def mark_as_paid(request):
    invoice = Invoice.objects.filter(invoice_number="LWP7854")
    invoice.update(is_paid=True)
    return JsonResponse({
        "success": True, 
        "message": f"Updated {invoice} invoice(s)."
    })