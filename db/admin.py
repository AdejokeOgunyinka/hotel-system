from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register((Booking, User, Room, Receptionist,
                     RoomStatus, RoomType, Reservation, Payment, PaymentType))
