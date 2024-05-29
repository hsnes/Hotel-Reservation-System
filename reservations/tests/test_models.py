from django.test import TestCase
from reservations.models import Hotel, Room, Reservation
from datetime import date

class ModelTests(TestCase):

    def setUp(self):
        self.hotel = Hotel.objects.create(
            name="Test Hotel",
            address="123 Test St",
            description="A hotel for testing"
        )
        self.room = Room.objects.create(
            hotel=self.hotel,
            number="101",
            type="Single",
            price_per_night=100.00
        )
        self.reservation = Reservation.objects.create(
            room=self.room,
            check_in=date(2023, 1, 1),
            check_out=date(2023, 1, 5),
            guest_name="John Doe",
            guest_email="john@example.com"
        )

    def test_hotel_creation(self):
        self.assertEqual(self.hotel.name, "Test Hotel")
        self.assertEqual(self.hotel.address, "123 Test St")

    def test_room_creation(self):
        self.assertEqual(self.room.number, "101")
        self.assertEqual(self.room.hotel.name, "Test Hotel")

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.guest_name, "John Doe")
        self.assertEqual(self.reservation.room.number, "101")
