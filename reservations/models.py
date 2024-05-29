from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.hotel.name} - Room {self.number}'


class Reservation(models.Model):
    room = models.ForeignKey(Room, related_name='reservations', on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()

    class Meta:
        unique_together = ['room', 'check_in', 'check_out']

    def __str__(self):
        return f'Reservation for {self.guest_name} from {self.check_in} to {self.check_out}'
