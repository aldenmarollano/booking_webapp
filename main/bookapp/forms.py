from django import forms
from bookapp.models import Bldg, Room, Booking

class BldgForm(forms.ModelForm):
    class Meta:
        model = Bldg
        fields = ['name', 'description', 'address']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'occupancy', 'building', 'price']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date']
            

