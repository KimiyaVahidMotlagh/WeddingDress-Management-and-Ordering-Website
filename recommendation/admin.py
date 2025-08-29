from django.contrib import admin
from .models import GeneratedImage, Measurement

admin.site.register(GeneratedImage)
admin.site.register(Measurement)