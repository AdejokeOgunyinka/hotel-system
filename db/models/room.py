import uuid
from django.db import models
from .room_type import RoomType
from .room_status import RoomStatus


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    room_type_id = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    room_status_id = models.ForeignKey('RoomStatus', on_delete=models.CASCADE)
    room_no = models.CharField(max_length=255)
    price = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        app_label="db"
