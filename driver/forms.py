from django import forms
from .models import Driver, Report

#Create your forms here

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    # subject = forms.CharField(max_length =100)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class FilterDrivers(forms.Form):
    class Meta:
        model = Driver
        exclude = ['first_name', 'last_name', 'bio', 'image', 'phonenumber','featured','rate']
        widgets = {
        'pro_skills':forms.CheckboxSelectMultiple(),
        'location':forms.CheckboxSelectMultiple(),
        }

class BookDriver(forms.Form):
    class Meta:
        model = Report
        exclude = ['transaction_id', 'driver_first_name', 'driver_last_name', 'driver_phonenumber', 'driver_rate','client_id','client_first_name','client_last_name','payment_status','payment_date']
