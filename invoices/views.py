from django.shortcuts import render,redirect
from .models import Invoice
from datetime import date
from django.http import JsonResponse
from django.utils import timezone
from .forms import InvoiceForm


def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            form = InvoiceForm()
            
            
        data = {
            'form':form
        }
        
        return render(request,'home.html',data)

# Create your views here.

current_date = date.today().isoformat()


def create_invoice(request):
    # Automatically creates and saves to the database
    invoice = Invoice.objects.create(
        customer_name="Pankaj Tripathi",
        invoice_number="LWP7854",
        invoice_amount=25000,
        date_created=timezone.now().date(),  # Ensures a valid date object
        is_paid=False
    )
    
    return render(request, "home.html", {})

def all_invoices(request):
    all_invoices = Invoice.objects.all()
    return all_invoices


def show(request):
    invoice = Invoice.objects.filter(invoice_number="LWP7854")
    return invoice


def mark_as_paid(request):
    try:
        # Fetches the single specific object
        invoice = Invoice.objects.get(invoice_number="LWP7854")
        invoice.is_paid = True
        invoice.save()
        
        return JsonResponse({
            "success": True, 
            "message": f"Invoice {invoice.invoice_number} marked as paid."
        })
    except Invoice.DoesNotExist:
        return JsonResponse({
            "success": False, 
            "message": "Invoice not found."
        }, status=404)