from django.contrib import admin
from .models import Hotel, Room, Reservation


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description')
    search_fields = ('name', 'address')


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'number', 'type', 'price_per_night')
    list_filter = ('hotel', 'type')
    search_fields = ('number', 'hotel__name')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'check_in', 'check_out', 'guest_name', 'guest_email')
    list_filter = ('check_in', 'check_out')
    search_fields = ('guest_name', 'guest_email', 'room__number')
