from django.http import HttpResponse
from django.shortcuts import render



def show_invoices(request):
    data = {
        "customer_name":"rahul",
        "invoice_total":15000,
    }
    
    return render(request,"cust_name.html",data)

def index(request):
    # return HttpResponse("Hello World, you are on the Invoice Page. Nice to have you all!")
    return render(request,"home.html")


def orders(request):
    customers = [
        {
            "customer_name": "Arpit Mishra",
            "product_purchased": "Wireless Mouse",
            "purchase_amount": 1299,
            "purchase_date": "2026-01-12",
            "order_delivered": True,
            "customer_home": "Jaipur"
        },
        {
            "customer_name": "Rahul Sharma",
            "product_purchased": "Bluetooth Speaker",
            "purchase_amount": 3499,
            "purchase_date": "2026-01-15",
            "order_delivered": True,
            "customer_home": "Delhi"
        },
        {
            "customer_name": "Priya Singh",
            "product_purchased": "Laptop Stand",
            "purchase_amount": 1899,
            "purchase_date": "2026-01-18",
            "order_delivered": False,
            "customer_home": "Mumbai"
        },
    ]
    
    
    return render(request,"orders.html",{"customers":customers})