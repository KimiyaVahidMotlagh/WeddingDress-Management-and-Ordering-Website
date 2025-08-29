from django.db import models
from django.contrib.auth.models import User
from dresses.models import Dress


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)
    date = models.DateField()  # قبلاً booking_date بود
    day_name = models.CharField(max_length=20, default="")  # پیش‌فرض خالی برای حل مشکل migrate

    def __str__(self):
        return f"{self.user.username} - {self.dress.name} - {self.date}"
