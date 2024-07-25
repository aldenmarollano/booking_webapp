from django.db import models
from django.contrib.auth.models import Permission

from account.models import Account
import os


def get_room_image_filepath(self, filename):
    image = os.path.basename(filename)
    return f'room_images/{image}'

def get_default_room_image():
    return 'default_image/default_profile.png'

class Bldg(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    occupancy = models.IntegerField()
    building = models.ForeignKey(Bldg, on_delete=models.CASCADE, related_name='building')
    price = models.DecimalField(max_digits=9, decimal_places=3, default=0)
    room_photo = models.ImageField(null=True, blank=True, upload_to=get_room_image_filepath, default=get_default_room_image)

    def __str__(self):
        return f'{self.name}, {self.building}'


class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


    def __str__(self):
        return f'{self.room} : {self.user}'


