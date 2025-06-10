from django.db import models
from django.contrib.auth.models import User
from dresses.models import Dress

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.dress.name} on {self.booking_date}"
