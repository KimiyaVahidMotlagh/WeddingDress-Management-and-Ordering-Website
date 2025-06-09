from django.db import models
from django.contrib.auth.models import User

class Measurement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bust = models.FloatField()
    waist = models.FloatField()
    hips = models.FloatField()
    height = models.FloatField()
    arm_length = models.FloatField()
    arm_width = models.FloatField()
    breast_shape = models.CharField(max_length=100)
