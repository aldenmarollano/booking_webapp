from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from bookapp.models import Booking, Room
DATETIME_FORMAT = "%m-%d-%Y %H:%M:%S"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S")
    end_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S")

    class Meta:
        model = Booking
        fields = ['user', 'room', 'start_date', 'end_date']
        

    def update(self, instance, validated_data):
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance




