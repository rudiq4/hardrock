from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['size', 'first_name', 'last_name', 'email', 'city', 'address',
                  'postal_code']
