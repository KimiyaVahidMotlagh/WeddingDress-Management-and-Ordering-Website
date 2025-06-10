from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['bust', 'waist', 'hips', 'height', 'arm_length', 'arm_width', 'breast_shape']
