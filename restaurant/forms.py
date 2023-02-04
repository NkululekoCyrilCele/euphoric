from django import forms
from .models import Bookings
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'reservation_date': 'Reservation Date',
            'reservation_slot': 'Reservation Slot'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'phone': PhoneNumberPrefixWidget(),
            'reservation_date': forms.DateInput(attrs={
                'class': 'forms-control'
            }),
            'reservation_slot': forms.NumberInput(attrs={
                'class': 'forms-control'
            }),
        }
