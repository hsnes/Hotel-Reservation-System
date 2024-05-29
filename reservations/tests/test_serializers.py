from django.test import TestCase
from reservations.models import Hotel, Room, Reservation
from reservations.serializers import HotelSerializer, RoomSerializer, ReservationSerializer
from datetime import date

class SerializerTests(TestCase):

    def setUp(self):
        self.hotel_data = {
            "name": "Test Hotel",
            "address": "123 Test St",
            "description": "A hotel for testing"
        }
        self.room_data = {
            "number": "101",
            "type": "Single",
            "price_per_night": 100.00
        }
        self.reservation_data = {
            "check_in": date(2023, 1, 1),
            "check_out": date(2023, 1, 5),
            "guest_name": "John Doe",
            "guest_email": "john@example.com"
        }

    def test_hotel_serializer(self):
        serializer = HotelSerializer(data=self.hotel_data)
        self.assertTrue(serializer.is_valid())
        hotel = serializer.save()
        self.assertEqual(hotel.name, "Test Hotel")

    def test_room_serializer(self):
        hotel = Hotel.objects.create(**self.hotel_data)
        room_data = self.room_data.copy()
        room_data['hotel'] = hotel.id
        serializer = RoomSerializer(data=room_data)
        self.assertTrue(serializer.is_valid())
        room = serializer.save()
        self.assertEqual(room.number, "101")

    def test_reservation_serializer(self):
        hotel = Hotel.objects.create(**self.hotel_data)
        room = Room.objects.create(hotel=hotel, **self.room_data)
        reservation_data = self.reservation_data.copy()
        reservation_data['room'] = room.id
        serializer = ReservationSerializer(data=reservation_data)
        self.assertTrue(serializer.is_valid())
        reservation = serializer.save()
        self.assertEqual(reservation.guest_name, "John Doe")
