from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Dress(models.Model):
    STATUS_CHOICES = [
        ("design", "In Design"),
        ("tailoring", "In Tailoring"),
        ("ready", "Ready"),
        ("shipped", "Shipped"),
    ]
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dresses')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="dresses/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "dress")
