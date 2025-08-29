from django.db import models
from django.contrib.auth.models import User


class GeneratedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='generated_images/')
    prompt = models.TextField()
    body_type = models.CharField(max_length=50, blank=True, null=True)
    sleeve = models.CharField(max_length=50, blank=True, null=True)
    neckline = models.CharField(max_length=50, blank=True, null=True)
    bodice = models.CharField(max_length=50, blank=True, null=True)
    skirt = models.CharField(max_length=50, blank=True, null=True)
    train = models.CharField(max_length=50, blank=True, null=True)
    structure = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class Measurement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bust = models.FloatField(default=0.0)
    waist = models.FloatField(default=0.0)
    hips = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    arm_length = models.FloatField(default=0.0)
    arm_width = models.FloatField(default=0.0)
    breast_shape = models.CharField(max_length=100, default="", blank=True)