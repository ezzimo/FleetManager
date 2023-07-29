from django import forms
from .models import SparePart

class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['name', 'description', 'quantity']
