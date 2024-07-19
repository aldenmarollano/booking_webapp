from django.db import models
from django.contrib.auth.models import Permission

from account.models import Account


class Bldg(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=500)

    user = Account.objects.get(username='admin')
    permission = Permission.objects.get(codename=['view_bldg', 'change_bldg', 'delete_bldg'])
    user.user_permissions.add(permission)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    occupancy = models.IntegerField()
    building = models.ForeignKey(Bldg, on_delete=models.CASCADE, related_name='building')
    price = models.DecimalField(max_digits=9, decimal_places=3, default=0)

    def __str__(self):
        return f'{self.name}, {self.building}'

class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_id')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_id')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.room} : {self.user}'


