from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Start Date")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="End Date")
