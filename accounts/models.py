from django.contrib.auth.models import User
from django.db import models


class BodyMeasurement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)
    bust = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    hips = models.FloatField(null=True, blank=True)
    body_type = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Measurement"
