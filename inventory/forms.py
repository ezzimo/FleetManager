from django import forms
from .models import Order, SparePart

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name', 'description', 'quantity']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['spare_part', 'quantity', 'order_date', 'expected_delivery_date', 'received_date', 'status']