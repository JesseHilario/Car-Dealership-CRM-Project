from django import forms
from .models import Car, Customer

class PurchaseTransactionForm(forms.Form):
    date_of_purchase = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sale_price = forms.DecimalField(max_digits=11, decimal_places=2)
    license_plate_state = forms.CharField(max_length=2)
    license_plate = forms.CharField(max_length=255)

    def __init__(self, *args, user=None, car=None, **kwargs):
        """Pass user and car objects when creating the form"""
        super().__init__(*args, **kwargs)
        self.user = user
        self.car = car

        # Automatically retrieve the car_id from the car object (previous page)
        if self.car:
            self.fields['car_id'] = forms.IntegerField(initial=self.car.car_id, widget=forms.HiddenInput())

        # Automatically retrieve the customer_id from the user (signed-in user)
        if self.user:
            try:
                customer = Customer.objects.get(l_name=self.user.last_name, phone_number=self.user.email)   # user.email is actually the phone number
                self.fields['customer_id'] = forms.IntegerField(initial=customer.customer_id, widget=forms.HiddenInput())
            except Customer.DoesNotExist:
                raise forms.ValidationError("No matching customer found.")
