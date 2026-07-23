from django import forms
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['customer_name','invoice_number','invoice_amount','is_paid']
        
    # Name must strictly match 'clean_<field_name>'
    def clean_invoice_amount(self):
        amount = self.cleaned_data.get('invoice_amount')
        if amount < 0:
            raise forms.ValidationError('Amount must be greater than zero')
        
        return amount
        