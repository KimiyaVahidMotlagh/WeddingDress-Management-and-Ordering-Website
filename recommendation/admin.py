from django.contrib import admin

from .models import Measurement

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'bust', 'waist', 'hips', 'height', 'arm_length', 'arm_width', 'breast_shape')
admin.site.register(Measurement, MeasurementAdmin)