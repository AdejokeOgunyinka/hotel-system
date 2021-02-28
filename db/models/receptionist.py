import uuid
from cloudinary.models import CloudinaryField
from django.db import models
from .user import User


class Receptionist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=10)
    avatar = CloudinaryField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        app_label="db"
