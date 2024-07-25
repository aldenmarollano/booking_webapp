from django import forms
from bookapp.models import Bldg, Room, Booking

class BldgForm(forms.ModelForm):
    class Meta:
        model = Bldg
        fields = ['name', 'description', 'address']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'occupancy', 'building', 'price', 'room_photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk and Bldg.objects.exists():
            self.fields['building'].initial = Bldg.objects.latest('id').pk


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user','room', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date>=end_date:
                raise forms.ValidationError("End date must be after start date.")

        return cleaned_data

            

