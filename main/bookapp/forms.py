from django import forms
from bookapp.models import Bldg, Room, Booking

class BldgForm(forms.ModelForm):
    class Meta:
        model = Bldg
        fields = ['name', 'description', 'address']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'occupancy', 'building']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date']

    def clean(self):
        if self.is_valid():
            user = self.cleaned_data['user']
            room = self.cleaned_data['room']
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']
            

