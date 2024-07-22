from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from bookapp.models import Booking, Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date']

    def create(self, validated_data):
        room_id = validated_data.pop('room')

        room_instance = Room.objects.get(pk=room_id['id'])

        booking_instance = Booking.objects.create(room=room_instance, **validated_data)
        return booking_instance


    def update(self, instance, validated_data):
        # read_only_fields = ['room']
        # Ensure read-only fields are not updated
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance




