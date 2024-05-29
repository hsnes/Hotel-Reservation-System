from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from reservations.models import Hotel, Room, Reservation
from datetime import date


class ViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()
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

    def test_get_hotels(self):
        response = self.client.get(reverse('hotel-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_hotel(self):
        data = {
            "name": "New Hotel",
            "address": "456 New St",
            "description": "A new hotel"
        }
        response = self.client.post(reverse('hotel-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hotel.objects.count(), 2)

    def test_create_conflicting_reservation(self):
        data = {
            "room": self.room.id,
            "check_in": date(2023, 1, 3),
            "check_out": date(2023, 1, 7),
            "guest_name": "Jane Doe",
            "guest_email": "jane@example.com"
        }
        response = self.client.post(reverse('reservation-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
