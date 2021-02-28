import uuid
from django.db import models
from .payment_type import PaymentType
from .receptionist import Receptionist
from .user import User


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    payment_type_id = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    customer_id = models.ForeignKey('User', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('Receptionist', on_delete=models.CASCADE)
    amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.customer_id} paid {self.amount}'
    

    class Meta:
        app_label="db"
