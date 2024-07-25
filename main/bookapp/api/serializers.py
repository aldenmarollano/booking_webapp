from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from bookapp.models import Booking, Room
DATETIME_FORMAT = "%m-%d-%Y %H:%M:%S"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    start_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S")
    end_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S")

    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date']

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if start_date and end_date:
            if start_date <= end_date:
                raise serializers.ValidationError("End date must be after start date.")
        return data

     




