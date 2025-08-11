from django import forms
from .models import BodyMeasurement
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']  # بدون password

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class BodyMeasurementForm(forms.ModelForm):
    class Meta:
        model = BodyMeasurement
        fields = ['height', 'bust', 'waist', 'hips']
        widgets = {
            'height': forms.NumberInput(attrs={'step': '0.1', 'min': '0'}),
            'bust': forms.NumberInput(attrs={'step': '0.1', 'min': '0'}),
            'waist': forms.NumberInput(attrs={'step': '0.1', 'min': '0'}),
            'hips': forms.NumberInput(attrs={'step': '0.1', 'min': '0'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)  # ایمیل اختیاری

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")