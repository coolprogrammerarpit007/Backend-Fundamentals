from django.db import models

# Create your models here.


#Invoice

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=50)
    invoice_amount = models.DecimalField(max_digits=10,decimal_places=2)
    date_created = models.DateField(auto_now_add=True) # once record created date will not change -> auto_now_add
    is_paid = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return f"Customer Name: {self.customer_name}, Invoice Number: {self.invoice_number} with Invoice Amount:{self.invoice_amount}! Created At: {self.date_created} is currently {'Paid' if self.is_paid else 'UnPaid'}"
    