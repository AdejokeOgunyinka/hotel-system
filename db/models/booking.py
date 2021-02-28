import uuid
from django.db import models
from .user import User
from .room import Room
from .receptionist import Receptionist
from .payment import Payment


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE)
    amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.customer_id} booked {self.room_id}'
    

    class Meta:
        app_label="db"
