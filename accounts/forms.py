import logging
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Customer
from django.db import transaction, IntegrityError

# Set up logging
logger = logging.getLogger(__name__)

class CustomSignupForm(UserCreationForm):
    f_name = forms.CharField(max_length=255, required=True, label="First Name")
    m_init = forms.CharField(max_length=1, required=False, label="Middle Initial", empty_value=None)
    l_name = forms.CharField(max_length=255, required=True, label="Last Name")
    phone_number = forms.CharField(max_length=10, required=True, label="Phone Number")
    email = forms.EmailField(max_length=255, required=False, label="Email", empty_value=None)
    apt_number = forms.CharField(max_length=255, required=False, label="Apartment Number", empty_value=None)
    street_number = forms.CharField(max_length=255, required=True, label="Street Number")
    city = forms.CharField(max_length=255, required=True, label="City")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'f_name', 'm_init', 'l_name', 'phone_number', 'apt_number', 'street_number', 'city']

    def save(self, commit=True):
        try:
            with transaction.atomic():  # Ensures atomicity
                # Save user first
                user = super().save(commit=False)
                user.first_name = self.cleaned_data['f_name']  # Save first name
                user.last_name = self.cleaned_data['l_name']  # Save last name
                user.email = self.cleaned_data['phone_number'] # Store phone number in email

                if commit:
                    user.save()  # Save user before linking to Customer

                # Create Customer instance linked to the user
                customer = Customer.objects.create(
                    f_name=self.cleaned_data['f_name'],
                    m_init=self.cleaned_data['m_init'],
                    l_name=self.cleaned_data['l_name'],
                    phone_number=self.cleaned_data['phone_number'],
                    email=self.cleaned_data['email'],
                    apt_number=self.cleaned_data['apt_number'],
                    street_number=self.cleaned_data['street_number'],
                    city=self.cleaned_data['city'],
                )

                return user

        except Exception as e:
            logger.error(f"Error creating user or customer: {e}")  # Log the actual error
            self.add_error(None, "An error occurred while creating the account. Please try again.")  # Generic user-friendly message
            return None  # Ensure no invalid user object is returned
