from django import forms
from django.forms import ModelForm
from .models import Booking, BookingTime
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    """
    Fields to be included in the booking form
    """
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone_number',
                  'date', 'time',)
        widgets = {
            'date': DateInput(),
            'empty_label': "Time"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """ Date picker calendar for booking form """
        self.fields['date'].widget.attrs['class'] = 'datepicker'

        """ Placeholders for the fields """
        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'date': 'Booking Date',
            'time': '',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 booking-form'
            self.fields[field].label = False
