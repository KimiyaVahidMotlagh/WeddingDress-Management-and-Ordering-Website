# recommendation/forms.py
from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['bust', 'waist', 'hips', 'height']  # فقط فیلدهای موجود
        labels = {
            'bust': 'Bust (cm)',
            'waist': 'Waist (cm)',
            'hips': 'Hips (cm)',
            'height': 'Height (cm)'
        }
        widgets = {
            'bust': forms.NumberInput(attrs={'placeholder': 'Enter bust measurement'}),
            'waist': forms.NumberInput(attrs={'placeholder': 'Enter waist measurement'}),
            'hips': forms.NumberInput(attrs={'placeholder': 'Enter hips measurement'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Enter height'})
        }